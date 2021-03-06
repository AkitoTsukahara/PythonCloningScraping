import scrapy
from CsvItem.item import CsvItem

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']
    item = []

    def parse(self, response):
        """
        ページから投稿のタイトルを全て抜き出し、次のページへのリンクがあればたどる
        """
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('a ::text').get()} # json
            # item = CsvItem()
            # item['no'] = '1'
            # item['title'] = title.css('a ::text').get()
            # yield item

        for next_page in response.css('a.next.page-numbers'):
            yield response.follow(next_page, self.parse)