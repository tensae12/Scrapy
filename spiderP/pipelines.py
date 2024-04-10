# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import logging
import pymongo


class MongodbPipeline:
    collection_name = 'transcripts'
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://tensae:pibmaG-gurzyz-0tosxy@cluster0.kmqrizq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client['My_Database']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item