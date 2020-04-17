import requests
from bs4 import BeautifulSoup
mainContent = requests.get("https://cryptonewsandprices.me/")
print(mainContent.text)
soup = BeautifulSoup(mainContent.text,'lxml')
title = soup.find('h5', class_='card-title').get_text()
print(title)