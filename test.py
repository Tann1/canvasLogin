from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.ohlone.edu/')
info = driver.find_element_by_xpath("//div[@id='block-menu-block-1']//li[contains(@class,'services')]//span[contains(@class,'drop')]")
time.sleep(1)
info.click()
info = driver.find_element_by_xpath("//div[@id='block-menu-block-1']//li[contains(@class,'services')]/ul/li[2]/a")
time.sleep(1)
info.click()
info = driver.find_element_by_xpath("//input[@id='username']")
time.sleep(1)
info.send_keys('UserName') #your canvas login
info = driver.find_element_by_xpath("//input[@id='password']")
time.sleep(1)
info.send_keys('Passoword') #your canvas password
info = driver.find_element_by_xpath("//form[@method='post']//button[@name='_eventId_proceed']")
time.sleep(1)
info.click()



