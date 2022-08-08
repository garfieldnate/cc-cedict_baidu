# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CedictBaiduItem(scrapy.Item):
    # query string
    query = scrapy.Field()
    # number of results
    result_count = scrapy.Field()
