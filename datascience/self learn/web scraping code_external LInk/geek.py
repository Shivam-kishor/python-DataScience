#step 0️⃣ 
#pip install requests
#pip install html5lib
#pip install bs4

#step 1️⃣ 
#from urllib import request
#import requests
#URL="https://www.geeksforgeeks.org/data-structures/" 
#r=requests.get (URL)
#print(r.content)   


'''
First of all import the requests library.
Then, specify the URL of the webpage you want to scrape.
Send a HTTP request to the specified URL and save the response from server in a response object called r.
Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.'''




#step 3️⃣ Parsing⬇
#This will not run on online IDE

#import requests
#from bs4 import BeautifulSoup
#URL="https://www.passiton.com/inspirational-quotes"
#r=requests.get(URL)
#soup=BeautifulSoup(r.content,'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())





"""We create a BeautifulSoup object by passing two arguments:

`
r.content : It is the raw HTML content.
html5lib : Specifying the HTML parser we want to use.
"""

#i installed install pip install parser-libraries


#step 4️⃣ 
#python program to scrape website
#and save quotes from website
#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
   
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
   
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'saved inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

'''import requests
from bs4 import BeautifulSoup
import csv
URL="http://www.values.com/inspirational-quotes"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
quotes=[] #a list to store quotes
table=soup.find('div',attrs={'id':'all_quotes'})
table=soup.findAll('div',attrs={'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):

quote={}
quote=['theme']=row.h5.text
quote=['url']=row.a['href']
quote['img']=row.img['alt'].split("#")[0]
quote['lines']=row.img['alt'].split("#")[1]
quotes["author"](quote)
filename='inspirational_quotes.csv'
with open(filename,'w',newline="") as f:
    w-csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
for quote in quotes:
    w.writerow(quote)


'''


