from selenium import webdriver
#from select import select
#import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_link_text("REGISTER").click()

driver.find_element_by_name("firstName").send_keys("Bisma")
driver.find_element_by_name("lastName").send_keys("Hasan")
driver.find_element_by_name("phone").send_keys("9587182144")
driver.find_element_by_name("userName").send_keys("hasan@gmail.com")
driver.find_element_by_name("address1").send_keys("xyz")
driver.find_element_by_name("city").send_keys("abc")
driver.find_element_by_name("state").send_keys("jdgdfhjdf")
driver.find_element_by_name("postalCode").send_keys("12345")

select = Select(driver.find_element_by_name('country'))
select.select_by_visible_text("ARUBA")
select.select_by_value("ARUBA")

driver.find_element_by_name("email").send_keys("xyzjkldjsfd")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_name("confirmPassword").send_keys("12345678")

#driver.find_element_by_name("submit").click()
