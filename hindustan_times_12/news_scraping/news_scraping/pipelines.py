# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.exceptions import DropItem  
from scrapy_jsonschema.item import JsonSchemaItem


class DuplicatesPipeline(object):  
   def __init__(self): 
      self.ids_seen = set() 

   def process_item(self, JsonSchemaItem, spider): 
      if JsonSchemaItem['heading'] in self.ids_seen: 
         raise DropItem("Repeated items found: %s" % JsonSchemaItem) 
      else: 
         self.ids_seen.add(JsonSchemaItem['heading']) 
         return JsonSchemaItem


class NewsScrapingPipeline:
        
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['news_paper_jsonschema_data']
        self.collection = db['hindu_tb']
    
    def process_item(self, item, spider):
        
        self.collection.insert(dict(item))
        return item


# from itemadapter import ItemAdapter

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
