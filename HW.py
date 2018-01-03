from selenium import webdriver
driver=webdriver.Chrome("H:\\Reference\\Python\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(20)

#driver.find_element_by_xpath(id="sign-in").click()
#driver.find_element_by_id("appleId").send_keys("dylankc@icloud.com")
driver.find_element_by_class_name("sbib_b").send_keys("Game of thrones")
#driver.find_element_by_id("pwd").send_keys("G@meofthrones00")
driver.find_element_by_id("pocs").click()
#driver.find_element_by_xpath(r"""/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div/button""").click()
# driver.find_element_by_xpath(r"""/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div/button""").click()
#//*[@id="sign-in"]
#//*[@id="appleId"]


