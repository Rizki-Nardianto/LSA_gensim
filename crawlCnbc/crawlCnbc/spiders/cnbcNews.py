from crawlCnbc.items import CrawlcnbcItem
import scrapy


class CnbcnewsSpider(scrapy.Spider):
    name = 'cnbcNews'
    start_urls = [
        # 'https://www.cnbc.com/2021/04/21/biden-advisor-brother-jeff-ricchetti-lobbied-white-house-on-behalf-of-health-care-firms.html'
        'https://www.cnbcindonesia.com/news/20210421181335-4-239729/cari-kapal-selam-hilang-tni-libatkan-singapura-australia'
    ]

    def parse(self, response):
        items = CrawlcnbcItem()

        berita = response.css('p::text').extract()

        items['berita'] = berita

        yield items
