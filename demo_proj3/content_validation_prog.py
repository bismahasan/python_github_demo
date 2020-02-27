from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/")

aboutus = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/a")
ouroffices = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/ul/li/a/span")
location = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/ul/li/ul/li[1]/a/span")

actions = ActionChains(driver)
actions.move_to_element(aboutus).move_to_element(ouroffices).move_to_element(location).click(location).perform()

window_before1 = driver.window_handles[0]
print(window_before1)

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)

driver.switch_to.frame("main_page")
obj = driver.find_element_by_id("demo3")
txt = obj.text
print(txt)
