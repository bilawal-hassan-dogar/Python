import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'  # Unique identifier for the spider
    start_urls = ['https://www.daraz.pk/smartphones/']  # URLs to start crawling from

    def parse(self, response):
        # Extract the title(s) from the response
        titles = response.css('title::text').extract()  # Note the use of ::text to get the text content
        
        # Iterate over the extracted titles and yield them individually
        for title in titles:
            yield {'titleTxt': title}

# To run this spider, you need to integrate it into a Scrapy project or use Scrapy's CLI
# For example, if you save this spider in a file named quotes_spider.py in your project's spiders folder,
# you can run it using:
# scrapy crawl quotes
