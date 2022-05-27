#!/usr/bin/env python3
from encodings import utf_8
coding: utf_8

#python script to download instagram image
#if used as jupyter notebook you need to run it as administrator and this notebook must be trusted
#the more stuff you do while running the script the more likely it will give you random errors and stop

from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import selenium.webdriver
import os.path
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())
#open instagram
driver.get("https://www.instagram.com")
#checks that cookies are there
if os.path.exists("D:\STARI\Documents\GitHub\InstaDown\cookies.pkl"):
    print("cookies retrieved")
else:
    print("cookies not found, please create cookie file first with cookie_creator.py")
    sys.exit()

#loads cookies
cookies = pickle.load(open("D:/STARI/Documents/GitHub/InstaDown/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)



#this checks that you have created a links_list.txt file before proceeding
#put the absolute path to your links_list.txt HERE
if os.path.exists("D:/STARI/Documents/GitHub/InstaDown/links_list.txt"):
    print("links_list.txt retrieved")
else:
    print("no links_list.txt found! please create a links list before proceeding!")
    sys.exit()

#you need to create a links_list.txt with all your Instagram URLs
#one line per URL, without adding anything else
#put the absolute path to your links_list.txt HERE
all_url = open("D:/STARI/Documents/GitHub/InstaDown/links_list.txt", "r")
data = all_url.read()
url_list = data.split("\n")
all_url.close()

print("Links read!")

time.sleep(0.3)

#iterating through list
#if interrupts simply erase downloaded URLs. you can see last download in browser
#last shown picture not downloaded unless download is not over
#gives error when finishes links_list.txt

for url in url_list:
    link_name = str(url.split("/")[-2])
    print(link_name)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img = soup.find('img', class_='FFVAD')
    img_url = img['src']
    r = requests.get(img_url)
    with open("'{}'.png".format(link_name),'wb') as f:
        f.write(r.content)
    time.sleep(0.7)