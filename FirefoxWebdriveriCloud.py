from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://www.icloud.com')

elem = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')