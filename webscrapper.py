from bs4 import BeautifulSoup
import requests

url = "https://www.daraz.pk/catalog/?spm=a2a0e.searchlist.search.2.404a294c0o9Fpe&q=car%20accesories&_keyori=ss&clickTrackInfo=textId--8612879763509792615__abId--None__pvid--db553e24-d6b5-4865-bc68-e36ece1409ae__matchType--1__abGroup--None__srcQuery--car%20accesories__spellQuery--car%20accesories__ntType--nt-common&from=suggest_normal&sugg=car%20accesories_1_1"
response = requests.get(url)
# print(response.content)

htmlcontent = response.content

# soup = BeautifulSoup(htmlcontent)
soup = BeautifulSoup(htmlcontent, "html.parser")

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)

# print(soup.find_all('a'))
# print(soup.find(id='beacon-aplus'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
    # print(image.get('src'))

products = soup.find_all('div', class_='ant-row main--pIV2h')
print(products)

products = soup.find_all('div', attrs={'class_':'ant-row main--pIV2h'})
print(products)


