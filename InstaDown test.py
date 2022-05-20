#!/usr/bin/env python3
from encodings import utf_8
coding: utf_8

#python script to download instagram image
#if used as jupyter notebook you need to run it as administrator and this notebook must be trusted
#the more stuff you do while running the script the more likely it will givwe you random errors and stop

from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#opens chrome window for user agent, need to go to instagram.com and login manually, for each session

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com")
print('You have one minute to login in the open Chrome window!')
time.sleep(60)

#you need to create a links_list.txt with all your Instagram URLs
#one line per URL, without adding anything else
#put the absolute path to your links_list.txt to prevent issues
#this transforms link_lists.txt in a list
all_url = open("D:\STARI\Downloads\links_list.txt", "r")

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
