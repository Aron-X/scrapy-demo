# -*- coding: utf-8 -*-
import codecs
import json


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class StackJsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('jobs.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


from scrapy.exporters import JsonItemExporter


class JsonExporterPipeline:
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        self.file = open('json_exporter.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        # 开启倒数
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
