'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
#import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/droppable/")
driver.switch_to_frame(0)
srce = driver.find_element_by_id("draggable")
trgt = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(srce, trgt).perform()