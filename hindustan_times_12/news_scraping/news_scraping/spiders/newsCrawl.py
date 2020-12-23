# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from news_scraping.items import NewsScrapingItem

class NewscrawlSpider(Spider):
    name = 'newsCrawl'
    start_urls = ['https://hindustantimes.com/']
    allowed_domain = ['hindustantimes.com']
    paths = ['.more-latest-news .headingfour a','.clearfix .para-txt a','.random-heading a','.new-assembly-elections a','.wclink2','.bigstory-mid-h3 a','.subhead4 a']
    # subheadings = ['figcaption','#miwInL23P7y8wYxwF1WiDL_story h2']
    summary = 'h2'
    topic = '.lok-sabha-elections-cb-sectionmr-15'
    headings = 'h1'
    imagelink = 'figure img'
    tags = '.topic-tags a'
    author = '.author'
    date = '.text-dt'
    #content = '/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div/div[4]//p/text()'
    content = '.storyDetail p'
    def parse(self, response):
        print("you are in 1")
        
        for path in self.paths:
            for url in response.css(path).css("::attr(href)").extract():
                if url is not None:
                    print(url)
                    req = Request(url=url , callback= self.parse_article)
                    yield req

        

    def parse_article(self,response):
        print("you are in 2")
        
        yield NewsScrapingItem({
            "topic": response.css(self.topic).css('::text').extract_first(),
            "heading": response.css(self.headings).css('::text').extract_first(),
            "imagelink": response.css(self.imagelink).css('::attr(src)').extract_first(),
            "summary" : response.css(self.summary).css('::text').extract_first(),
            "date_published" : response.css(self.date).css('::text').extract_first(),
            "author" : response.css(self.author).css('::text').extract_first(),
            "content" : [content[:6000] for content in response.css(self.content).css('::text').extract()],
            "tags" : [tag for tag in response.css(self.tags).css('::text').extract()]
        })
        
        
        
        # for subheading in self.subheadings:
        #     for word in response.css(subheading).css('::text').extract():
        #         l.add_value('subheading', word)





