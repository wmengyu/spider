# -*- coding: utf-8 -*-
import scrapy

from movie.items import MovieItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 找到所有的电影
        table_list = response.xpath('//div[@class="co_content8"]/ul//table')
        for table in table_list:
            # 创建对象
            item = MovieItem()
            item['name'] = table.xpath('.//a[@class="ulink"]/text()').extract_first()
            item['move_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
            # 获取电影详细信息页面链接
            movie_url = 'http://www.ygdy8.net' + table.xpath('.//a[@class="ulink"]/@href').extract_first()
            # print(move_url)
            # yield item
            yield scrapy.Request(url=movie_url, callback=self.next_page, meta={'item': item})

    # 获取item其它信息
    def next_page(self, response):
        # 获取传递过来的参数
        item = response.meta['item']
        item['img_url'] = response.xpath('//div[@id="Zoom"]//p/img[1]/@src').extract_first()
        item['download_url'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()
        yield item
