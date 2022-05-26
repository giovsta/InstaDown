import pickle
import selenium.webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com")
print("you have 20 seconds to login")
time.sleep(20)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
print("cookie created!")