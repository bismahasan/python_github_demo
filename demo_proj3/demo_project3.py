from selenium import webdriver
#from selenium.webdriver.common.keysimport import keys
import time

print ("hello world");
driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(2)
driver.find_element_by_name("btnK").click()