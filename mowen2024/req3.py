import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Version 125.0.6422.142 
# 114.0.5735.90
# https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/win64/chromedriver-win64.zip
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# https://www.jb51.net/python/304442ttz.htm#_label0

# r"C:\apps\chromedriver-win64-125.0.6422"
driver = webdriver.Chrome()
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()