#web scraping using python & BeautifulSoup


#if u want to scrape a website

#1 use the API
#2 HTML Web Scraping using some tool like bs4


# STEP 0 ➡️library used
#pip install requests
#pip install  html5lib  
#pip install    bs4

import requests
#import urllib2
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#STEP 1 ➡️ get the html 
r = requests.get(url)
htmlContent=r.content
#print(htmlContent)


# STEP 2 ➡️ Parse then HTMl 
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup)
# STEP 2 ➡️ HTML Tree Travrsal