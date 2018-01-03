import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.icloud.com')
#assert 'Yahoo!' in browser.title
browser.implicitly_wait(90)
elem = browser.find_element_by_id("appleId")
browser.implicitly_wait(40)
elem.send_keys('seleniumhq' + Keys.RETURN)
browser.implicitly_wait(90)
browser.quit()