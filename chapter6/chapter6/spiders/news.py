import scrapy

from chapter6.items import Headline  # ItemのHeadlineクラスをインポート。


class NewsSpider(scrapy.Spider):
    name = 'news'  # Spiderの名前。
    allowed_domains = ['news.yahoo.co.jp']  # クロール対象とするドメインのリスト。
    start_urls = ['https://news.yahoo.co.jp/']  # クロールを開始するURLのリスト。

    def parse(self, response):
        """
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出してたどる。
        """
        for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
            yield response.follow(url, self.parse_topics)

    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す。
        """
        item = Headline()  # Headlineオブジェクトを作成。
        item['title'] = response.css('.tpcNews_title::text').get()  # タイトル
        item['body'] = response.css('.tpcNews_summary').xpath('string()').get()  # 本文
        yield item  # Itemをyieldして、データを抽出する。
