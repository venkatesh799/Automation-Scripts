# Author : Venkatesh Thirunagiri

#importing Selenium Webdriver
from selenium import webdriver 

#import getpass module - to hide the password
from getpass import getpass

username=input("Enter Your Facebook Username   :")
password=getpass("Enter Your Facebook Password   :")
driver=webdriver.Chrome("Chrome Webdriver Path")
driver.get("https://www.facebook.com/")
username_id=driver.find_element_by_id('email')
username_id.send_keys(username)
password_id=driver.find_element_by_id('pass')
password_id.send_keys(password)
login=driver.find_element_by_id('loginbutton')
login.submit()
