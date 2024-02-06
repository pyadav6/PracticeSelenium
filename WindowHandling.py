from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")

driver.switch_to.new_window('tab')

driver.get("https://www.amazon.com")

print(driver.window_handles)

driver.switch_to_default_content()

driver.implicitly_wait(5)

driver.close()
