#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python script to download instagram image
#if used as jupyter notebook you need to run it as administrator and this notebook must be trusted
#the more stuff you do while running the script the more likely it will givwe you random errors and stop
get_ipython().run_line_magic('pip', 'install webdriver-manager')


# In[ ]:


from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#one day all the code below will allow you to use your cookies to login
#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--user-data-dir=chrome-data")
#driver = webdriver.Chrome(options=chrome_options)
#driver.get('https://www.instagram.com')  # Already authenticated
import time


# In[ ]:

#opens chrome window for user agent, need to go to instagram.com and login manually, for each session
#maybe cause I have Chrome in research mode
#driver = webdriver.Chrome('chromedriver')

driver = webdriver.Chrome(ChromeDriverManager().install())


# In[ ]:


#you need to create a link_list.txt with all your Instagram URLs
#one line per URL, without adding anything else. or change "\n"

#this transforms link_lists.txt in a list
all_url = open("links_list.txt", "r")

data = all_url.read()

url_list = data.split("\n")

for item in url_list:
    print(item)

all_url.close()

#iterating through list
#if interrupts simply erase downloaded URLs. you can see last download in browser
#last shown picture not downloaded if download is not over
# gives error when finishes links cause who cares

#one day this thing will rename files to images that make actual sense

for i in url_list:
    driver.get(i)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img = soup.find('img', class_='FFVAD')
    img_url = img['src']
    r = requests.get(img_url)
    string = str(img_url)
    with open("instagram"+str(time.time())+".png",'wb') as f:
        f.write(r.content)

