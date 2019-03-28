import urllib.request as ul
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# copyright is included in every articles so it has to be remove
cr = 'Copyright © 2018. Jang Group of Newspapers All rights reserved.'

#Starting page
pg = 100

#Articles Source URL
url = 'https://jang.com.pk/roman/news/'

articles=[]



# Saving Corpus to a .txt file. It is called after getData() function to save articles.
def saveFile(my_list):

    with open('your_file.txt', 'w',encoding="UTF-8") as f:
        for item in my_list:
            f.write("%s\n" % item)

            


#Main data scrapping function
def getData():

    global articles

    #the number in range function defines the number of articles to crawl
    for i in range (30):

        print(i)

        #Increments the article number as all the articles are in a sequence
        quote_page = url + str(pg + i)

        #connects to the url above
        page = ul.urlopen(quote_page)

        #Beautiful Soup library is used for crawling the url
        soup = BeautifulSoup(page, 'html.parser')

        #This function arranges the data in a neat format
        soup.prettify()

        #The "p" tag corresponds to the main article text, so the function only extracts the main text
        for rt in soup.find_all('p'):
            text = rt.get_text()

            #removes copy right 
            text = text.replace(cr,'')

            #removes irrelevant tag
            text = text.replace('\xa0','')

            #Collects all articles in a single list. 
            if text != '' and text != '\xa0':
                articles.append(text)


            
