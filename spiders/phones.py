# -*- coding: utf-8 -*-
import scrapy


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['www.mysite.com']
    start_urls = ['https://www.mysite.com']

    def parse(self, response):
        for urun in response.xpath("//p[@class='image-container']"):
            yield{
                "alt" : urun.css('img').attrib['alt'],
                "src" : urun.css('img').attrib['src'] 
            } 


""" 
src = resimler[1].css('img').attrib['src']  
alt = resimler[1].css('img').attrib['alt'] 
-----------
response.css('img').attrib['src']
//p[@class='image-container']
"""

# python -m scrapy crawl phones
# python -m scrapy crawl phones -o example.json