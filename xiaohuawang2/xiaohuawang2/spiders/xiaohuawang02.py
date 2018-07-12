# -*- coding: utf-8 -*-
import scrapy

from xiaohuawang2.items import Xiaohuawang2Item


class Xiaohuawang02Spider(scrapy.Spider):
    name = 'xiaohuawang02'
    allowed_domains = ['www.xiaohuar.com']
    url = 'http://www.xiaohuar.com/list-1-'
    page = 0
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']

    def parse(self, response):
        #解析数据获取所有校花
        div_list = response.xpath('//div[@class="item masonry_brick"]')
        for div in div_list:
            item = Xiaohuawang2Item()
            img_url = div.xpath('./div[@class="item_t"]/div[@class="img"]/a/img/@src').extract_first()
            # print(img_url)
            # 处理周半仙图片
            if img_url.endswith('.php'):
                img_url = img_url.replace('.php', '.jpg')
            img_url = 'http://www.xiaohuar.com' + img_url
            # print(img_url)
            name = div.xpath('./div[@class="item_t"]/div[@class="img"]/span[@class="price"]/text()').extract_first()
            school = div.xpath('./div[@class="item_t"]/div[@class="img"]/div[@class="btns"]/a/text()').extract_first()
            like = div.xpath('./div[contains(@class,"item_b")]//em[@class="bold"]/text()').extract_first()
            # 将数据保存到对象中
            item['img_url'] = img_url
            item['name'] = name
            item['school'] = school
            item['like'] = like
            # 将该对象进行返回
            yield item
        # 当处理第2页或者其他页  是不是要接着发送请求进行处理
        self.page += 1
        if self.page <=43:
            url = self.url + str(self.page) +'.html'
            yield scrapy.Request(url=url, callback=self.parse)

