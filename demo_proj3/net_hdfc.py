'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time 

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")
window_before1 = driver.window_handles[0]

print(window_before1)
title1 = driver.title
print(title1)

driver.switch_to_frame(1)
driver.find_element_by_link_text("Privacy Policy").click()
print("clicked on PP")
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
privacy_title = driver.title
print(privacy_title)
driver.find_element_by_link_text("Personal").click()
print("clicked on personal")
driver.switch_to.window(window_before1)
time.sleep(2)
driver.switch_to.frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("444378")
time.sleep(2)
driver.quit()
