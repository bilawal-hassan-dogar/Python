import scrapy
from pathlib import Path
import logging

class Bookspider(scrapy.Spider):
    name = 'Books'
    start_urls = ['https://toscrape.com']

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        # a = response.css(".product_pod").get()
        # b = a.css("a")
        # print(b)

# To run this spider, ensure it's integrated into a Scrapy project or use Scrapy's CLI
