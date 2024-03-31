import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback="parse_item", follow=True),
        )

    def parse_item(self, response):
       print(response.url)
