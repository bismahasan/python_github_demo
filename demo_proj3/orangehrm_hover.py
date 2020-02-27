'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()

time.sleep(2)

admin = driver.find_element_by_id("menu_admin_viewAdminModule")
user_man = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_man).move_to_element(users).click(users).perform()
