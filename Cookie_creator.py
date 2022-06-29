import pickle
import selenium.webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass

# initialize the browser
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)

#go to website
driver.get("https://instagram.com")
time.sleep(0.5)

#get rid of cookie banner
driver.find_element(By.XPATH, "//button[@class='aOOlW   HoLwm ']").click()
time.sleep(0.5)

# Instagram credentials
my_username = getpass.getpass("Insert Instagram username (input hidden for safety concerns):")
while True:
    try:
        my_username = my_username 
        if my_username!= "":
            print("username stored")
            break;
        else:
            print("username not stored")
            break;
    except ValueError:
        print("Invalid")
        continue

my_password = getpass.getpass('Insert your password here (input hidden for safety concerns):')

while True:
    try:
        my_password = my_password 
        if my_password!="":
            print("password stored!")
            break;
        else:
            print("password not stored")
            break;
    except ValueError:
        print("Invalid")
        continue

#insert username
driver.find_element(By.NAME, "username").send_keys(my_username)
time.sleep(0.5)

#insert password
driver.find_element(By.NAME, "password").send_keys(my_password)
time.sleep(0.5)

#login
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
time.sleep(5)

#create cookie file
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
print("cookie created!")