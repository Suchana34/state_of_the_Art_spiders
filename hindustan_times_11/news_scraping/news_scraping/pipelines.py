# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.exceptions import DropItem  

from itemadapter import ItemAdapter

class DuplicatesPipeline(object):  
   def __init__(self): 
      self.ids_seen = set() 

   def process_item(self, item, spider): 
      if item['heading'] in self.ids_seen: 
         raise DropItem("Repeated items found: %s" % item) 
      else: 
         self.ids_seen.add(item['heading']) 
         return item

# class filterPipelines(object):
#    def __init__(self):

#    def process_item(self, item, spider):


class NewsScrapingPipeline:
        
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['news_paper_dec_data']
        self.collection = db['hindu_tb']
    
    def process_item(self, item, spider):
        
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item


# class MongoPipeline:

#     collection_name = 'scrapy_items'

#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
#         )

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
#         return item
