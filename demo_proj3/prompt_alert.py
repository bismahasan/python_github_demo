'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
loc = "C:\python_selenium_practice\confirmation_alert.html"
driver.get(loc)

continuebtn = driver.find_element_by_name("employeeLogin").click()

obj = driver.switch_to.alert
str1 = obj.text
print(str1)
time.sleep(2)

obj.send_keys("bisma")
time.sleep(2)
obj.accept()
obj.accept()