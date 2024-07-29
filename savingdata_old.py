from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=car+accessories&sid=1mt%2Cbpx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=car+accessories%7CCar+Air+Purifiers+and+Air+Fresheners&requestId=35550a7d-5b46-47d5-b3ef-e37adc55aa97&as-backfill=on"
response = requests.get(url)


htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, "html.parser")

titles = []
prices = []
images = []

for f in soup.find_all('div', attrs={"class":"_75nlfW"}):
    print(f)