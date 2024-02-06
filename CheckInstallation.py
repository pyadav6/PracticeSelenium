# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

 
# create webdriver object
driver = webdriver.Chrome()

# get google.com
driver.get("https://google.com")

#print title of the page
print(driver.title)

#searching for search bar on the page
searchbar = driver.find_element("xpath", '//*[@id="APjFqb"]')

#clear any prior value
searchbar.clear()

#Searching for python tutorials
searchbar.send_keys("Good python programs to practice")

#click enter for serach to begin
searchbar.send_keys(Keys.RETURN)

#To print the current url of the page
print(driver.current_url)

driver.close()