# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy_jsonschema.item import JsonSchemaItem


class NewsScrapingItem(JsonSchemaItem):
    jsonschema =     {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": "News",
        "description": "from news site",
        "type": "object",
        "properties": {
            "heading": {
                "description": "heading of the news",
                "type": "string"
            },
            "author": {
                "description": "author of the news",
                "type": "string"
            },
            "summary": {
                "description": "summary of the news",
                "type": "string"
            },
            "imagelink": {
                "description": "image link of the news",
                "type": "string"
            },
            "topic": {
                "description": "topic of the news",
                "type": "string"
            },
            "tags": {
                "description": "tags of the news",
                "type": "array"
            },
            "date_published": {
                "description": "date_published of the news",
                "type": "string"
            },
            "content": {
                "description": "content of the news",
                "type": "array"
            }
        },
        "required": ["heading", "content", "tags", "topic", "imagelink", "summary", "author", "date_published"]
    }


    
# class NewsScrapingItem(ValidateItem):
    
#     heading = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(str.strip, remove_quotations, remove_nt),
#         output_processor= TakeFirst()
#     )
#     author = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
#         output_processor= Join(',')
#     )
#     subheading = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
#         output_processor= Join(',')
#     )
#     imagelink = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
#         output_processor= TakeFirst()
#     )
#     summary = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
#         output_processor= Join(',')
#     )
#     date_published = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
#         output_processor= TakeFirst()
#     )
#     content = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
#         output_processor= Join(',')
#     )
#     topic = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
#         output_processor= Join(',')
#     )
#     tags = scrapy.Field(
#         default = "none",
#         input_processor= MapCompose(remove_tags, remove_quotations, remove_nt),
#         output_processor= Join(',')
#     )

