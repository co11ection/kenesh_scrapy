# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KeneshScraoyItem(scrapy.Item):
    name  = scrapy.Field()
    number = scrapy.Field
    mail = scrapy.Field()
    fraction = scrapy.Field()