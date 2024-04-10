import logging 
import pymongo


class MongodbPipline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("")
        self.db = self.client['My_Database']

    def close_spider(self, spider):
        logging.warning('Spider Closed - Pipeline')

    def process_item(self, item, spider):
        return item