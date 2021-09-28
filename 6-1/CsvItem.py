import scrapy

class CsvItem(scrapy.Item):
  	no = scrapy.Field()
    title = scrapy.Field()
