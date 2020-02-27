from selenium import webdriver
import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
loc = "C:\python_selenium_practice\simple_alert.html"
driver.get(loc)

button = driver.find_element_by_name('alert')
button.click()

obj = driver.switch_to_alert()

msg = obj.text
print("Alert shows following message: " + msg)
time.sleep(2)
