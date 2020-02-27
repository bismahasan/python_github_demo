'''
Created on Feb 25, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from select import select
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
driver.find_element_by_name("userName").send_keys("bismahasan")
driver.find_element_by_name("firstName").send_keys("Bisma")
driver.find_element_by_name("lastName").send_keys("Hasan")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_name("confirmPassword").send_keys("12345678")
driver.find_element_by_xpath("//input[@value='Female']").click()
driver.find_element_by_name("emailAddress").send_keys("hasanbisma123@gmail.com")
driver.find_element_by_name("mobileNumber").send_keys("1234567891")
#driver.find_element_by_name("dob").send_keys("12/12/1995")
driver.find_element_by_xpath("//img[@alt='Ch']").click()
select2 = Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select2.select_by_visible_text('May')
select3 = Select(driver.find_element_by_xpath("//select[@data-handler='selectYear']"))
select3.select_by_visible_text('1998')
driver.find_element_by_xpath("//a[contains(.,'23')]").click()

driver.find_element_by_name("address").send_keys("123, qutub minar, dilli")
select = Select(driver.find_element_by_name('securityQuestion'))

select.select_by_visible_text('What is your favour color?')
time.sleep(2)
select.select_by_value("411011")
driver.find_element_by_name("answer").send_keys("pink")
#driver.find_element_by_name("btnK").click()