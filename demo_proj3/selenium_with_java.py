'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("selenium download")
time.sleep(2)
driver.find_element_by_name("btnK").click()
driver.find_element_by_xpath("a[@href='https://www.selenium.dev/downloads/']")
driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[6]/a[4]")
#driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
driver.switch_to_default_content()
time.sleep(2)
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
driver.switch_to_default_content()
time.sleep(2)
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("OutputType").click()
driver.switch_to_default_content()