from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the URL
driver.get("https://www.flipkart.com/search?q=car+accessories&sid=1mt%2Cbpx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=car+accessories%7CCar+Air+Purifiers+and+Air+Fresheners&requestId=35550a7d-5b46-47d5-b3ef-e37adc55aa97&as-backfill=on")

# Wait for the page to load
driver.implicitly_wait(10)

# Get the page source
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

titles = []
prices = []
images = []

# Assuming the class name is correct and the elements exist
for f in soup.find_all('div', attrs={"class": "_75nlfW"}):
    # Process each element as needed
    print(f)

# Close the driver
driver.quit()
