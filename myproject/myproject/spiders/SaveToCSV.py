import scrapy
from pathlib import Path
import datetime
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Mobilespider(scrapy.Spider):
    name = 'GPT_Spider'
    start_urls = ['https://www.daraz.pk/smartphones/']

    def __init__(self, *args, **kwargs):
        super(Mobilespider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Initialize CSV file
        self.csv_file = open('mobiles_data.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Page', 'Title', 'Price', 'Sold', 'Date'])

    def start_requests(self):
        urls = [
            "https://www.daraz.pk/smartphones/?page=1",
            "https://www.daraz.pk/smartphones/?page=2",
            "https://www.daraz.pk/smartphones/?page=3",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        
        # Wait for dynamic content to load
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".Bm3ON"))
            )
        except Exception as e:
            self.log(f"Error: {e}")

        html = self.driver.page_source
        response = scrapy.http.TextResponse(url=response.url, body=html, encoding='utf-8')
        
        page = response.url.split("page=")[-1]
        containers = response.css(".Bm3ON")

        for container in containers:
            title = container.css('.Ms6aG > .qmXQo > .buTCk > .RfADt > a::text').get()
            price = container.css('.Ms6aG > .qmXQo > .buTCk > .aBrP0 > .ooOxS::text').get()
            sold = container.css('.Ms6aG > .qmXQo > .buTCk > ._6uN7R > ._1cEkb > span::text').get()

            # Write to CSV file
            self.csv_writer.writerow([page, title, price, sold, datetime.datetime.now(tz=datetime.timezone.utc)])

    def closed(self, reason):
        self.driver.quit()
        self.csv_file.close()
