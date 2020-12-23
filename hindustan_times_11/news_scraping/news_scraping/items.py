# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import re

from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


from scrapy_jsonschema.item import JsonSchemaItem


def remove_quotations(value):
    return value.replace(u"\u201d", '').replace(u"\u201c", '')

def remove_nt(value):
    return value.replace("\n",' ').replace(" ", " ")

def filter_value(value):
    if re.sub("[^0-9]", "", value):
        return value
    else:
        return None
#this is the code for removing all text

def filter_num(value):
    if value.isalnum():
        return value[0]
    else:
        return 0

# def remove__whitespace(value):
#     return value.strip()


class ValidateItem(JsonSchemaItem):
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
            "subheading": {
                "description": "subheading of the news",
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
                "type": "string"
            },
            "date_published": {
                "description": "date_published of the news",
                "type": "string"
            },
            "tags": {
                "description": "tags of the news",
                "type": "string"
            },
            "content": {
                "description": "content of the news",
                "type": "string"
            }
        },
        "required": ["heading", "subheading", "content", "tags", "topic", "imagelink", "summary", "author", "date_published"]
    }


    
class NewsScrapingItem(ValidateItem):
    
    heading = scrapy.Field(
        default = "none",
        input_processor= MapCompose(str.strip, remove_quotations, remove_nt),
        output_processor= TakeFirst()
    )
    author = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
        output_processor= Join(',')
    )
    subheading = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
        output_processor= Join(',')
    )
    imagelink = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
        output_processor= TakeFirst()
    )
    summary = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
        output_processor= Join(',')
    )
    date_published = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
        output_processor= TakeFirst()
    )
    content = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_quotations, remove_nt),
        output_processor= Join(',')
    )
    topic = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, str.strip, remove_nt, remove_quotations),
        output_processor= Join(',')
    )
    tags = scrapy.Field(
        default = "none",
        input_processor= MapCompose(remove_tags, remove_quotations, remove_nt),
        output_processor= Join(',')
    )
    flag = scrapy.Field(
        default = "none",
        input_processor = MapCompose(remove_nt, remove_quotations, remove_tags),
        output_processor = TakeFirst()
    )

