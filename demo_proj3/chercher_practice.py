'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
menu = driver.find_element_by_id("sub-menu")
google_link = driver.find_element_by_id("link2")

actions = ActionChains(driver)
actions.move_to_element(menu).move_to_element(google_link).click(google_link).perform()
time.sleep(2)
driver.back()

actions1 = ActionChains(driver)
double_click1 = driver.find_element_by_id("double-click")
actions1.double_click(double_click1).perform()

alert = driver.switch_to_alert()
str1 = alert.text
print(str1)
alert.accept()