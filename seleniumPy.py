import time
from selenium import webdriver
driver = webdriver.Chrome("H:\\Reference\\Python\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.yellowpages.com.au/")
driver.maximize_window()
#driver.implicity_wait(20)
input("how old are you")
print(input)