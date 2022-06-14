#-------------------------------------------------------------------------------
# Name:        Image Downloader 
# Purpose:     To download images and save links of any image from any website link
#
# Author:      Heccubernny
#
# Created:     17/04/2020
# Copyright:   (c) Heccubernny 2020
# Licence:     CRSPIP licence
#-------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import urllib.request


url = input("Paste the website url here: ")

#To avoid the website from blocking you 
#Visit https://curl.trillworks.com/
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

#Know let make our request from the website

res = requests.get(url=url, headers=headers)
#To confirm that the website wont block you.
#Type print(res)

#Now we are going to use beautiful soup
soup = BeautifulSoup(res.text, 'html.parser')

for index, img in enumerate(soup.findAll('img'), start=1):
    #To fetch all the images sources code on the website type print(img)
    img_t = img.get('src')
    #To fetch for the link for the images type print(img_t)
    img_path = url + img_t if img_t[:1] == '/' else img_t
    print(img_path)

    if '.png' in img_path:
        with open(f"{index}.png", 'wb') as saveImg:
            saveImg.write(requests.get(url = img_path).content)
        print(img_path)


    #Later on i will work on where to save the images AND also saving all the images in a txt file
    #In the later version i will produce an application which will make it a cross platform