from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the URL
driver.get("https://www.daraz.pk/smartphones/")

# Wait for the page to load
driver.implicitly_wait(10)

# Get the page source
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

titles = []
prices = []
images = []

# Assuming the class names are correct and the elements exist
for d in soup.find_all('div', attrs={'class':'gridItem--Yd0sa'}):
    title = d.find('div', attrs={'class': 'title-wrapper--IaQ0m'})
    price = d.find('span', attrs={'class': 'currency--GVKjl'})
    image = d.find('img', attrs={'class': 'image--Smuib'})

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

# Define the CSV file name
filename = 'Mobile.csv'

# Open the file in write mode ('w')
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(['Title', 'Price', 'Image Link'])
    
    # Write the rest of the rows
    for i in range(len(titles)):
        csvwriter.writerow([titles[i], prices[i], images[i]])

# Close the driver
driver.quit()

print(f'Data has been written to {filename} Successfully')
