import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python','Здоровье','Физика'}


response = requests.get('https://habr.com/')
response.raise_for_status()

soup = BeautifulSoup(response.text, features = 'lxml')
articles = soup.find_all('article')
for article in articles:
    header= article.find('h2').text
    print(header)
print(len(articles))



soup = BeautifulSoup(response.text, features = 'html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('span', class_="tm-article-snippet__hubs-item")
    hubs = set([hub.find('span').text for hub in hubs])
    print(hubs)
    if KEYWORDS & hubs:
        print("---"*10)
        header = artcile.find('h2').text
        print(header)