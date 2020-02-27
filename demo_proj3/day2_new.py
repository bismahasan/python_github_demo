from selenium import webdriver

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")

driver.switch_to_frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("75668936")
driver.switch_to_default_content()

driver.switch_to_frame("footer")
driver.find_element_by_link_text("Privacy Policy").click()
driver.switch_to_default_content()

driver.switch_to_frame("login_page")
driver.find_element_by_xpath("//img[@alt='continue']").click()
#driver.find_element_by_name("btnK").click()