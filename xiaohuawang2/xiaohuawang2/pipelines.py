# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Xiaohuawang2Pipeline(object):
    #重写初始化动作
    def __init__(self):
        #此函数只会执行一次
        self.fw = open('xiaohua.json', 'w', encoding='utf-8')

    #处理每一个item
    def process_item(self, item, spider):
        #将item对象转化为字典
        obj = dict(item)
        #将对象转化为字符串
        str = json.dumps(obj, ensure_ascii=False)
        self.fw.write(str + '\n')
        return item

    #重写关闭方法 关闭spider的时候关闭资源文件
    def close_spider(self, spider):
        self.fw.close()