#-------------------------------------------------------------------------------
# Name:        Downloading link
# Purpose:     To download anything from a website link
#
# Author:      Heccubernny
#
# Created:     29/03/2020
# Copyright:   (c) Heccubernny 2020
# Licence:     CRSPIP licence
#-------------------------------------------------------------------------------

import requests
link = input("Copy and paste the link here --> ")
res = requests.get(link)
res.raise_for_status()
save = input("Enter the name you wish to save the file --> ")
fort = input("Enter the format you want to save it as --> ")
saveFile = open(save+'.'+fort, 'wb')
for start in res.iter_content(10000000):
    saveFile.write(start)
saveFile.close()
