import requests, bs4
res = requests.get('https://hetechpom.blogspot.com/2020/01/how-to-use-100-naira-recharge-card-per.html')
noStarchSoup = bs4.BeautifulSoup()
show = noStarchSoup.select('#author')
type(show)