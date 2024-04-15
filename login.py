from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time

# Accessing the yaml file for stored username and password
conf = yaml.safe_load(open('E:/project/auto_login/login_Details.yml'))
# Retriving username and password from yaml file 
#and storing in local variables
username = conf['username']
password = conf['password']

#Initializing instance of crome driver
driver = webdriver.Chrome()

#Opeaning website
driver.get('url_of_website')

#Finding username and password field in webpage 
#and storing their id in local variables
username_field = driver.find_element(By.ID, "TxtUserName")    
password_field = driver.find_element(By.ID, "TxtPassword")
    
#Enter the username and password
username_field.send_keys(username)
password_field.send_keys(password)

#Finding submit button in webpage 
#and storing its id in local variables
button = driver.find_element(By.ID,"btnLogin")

# Click the login button
button.click()

#time delay before closing the website
time.sleep(5)

#take screnshot 
driver.save_screenshot('E:/project/auto_login/screenshot.png')



