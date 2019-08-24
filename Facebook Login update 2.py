# Author Venkatesh Thirunagiri

# Facebook Login Script and Scrolling the News Feed Automatically

#importing Selenium
from selenium import webdriver
import time
from getpass import getpass
username=input("Enter Your Facebook Username   :")
password=getpass("Enter Your Facebook Password   :")
driver=webdriver.Chrome("Chrome Webdriver path")
driver.get("https://www.facebook.com/")
driver.maximize_window()
username_id=driver.find_element_by_id('email')
username_id.send_keys(username)
password_id=driver.find_element_by_id('pass')
password_id.send_keys(password)
login1=driver.find_element_by_id('loginbutton')
login1.submit()
height=driver.execute_script("return document.body.scrollHeight") 
x,y=0,300
time.sleep(4)
while height > y:
    driver.execute_script("window.scrollTo({0},{1})".format(x,y))  # scrolling to bottom
    x=y
    y=y+300
    time.sleep(5)  # wait for 5 seconds to read news feed
    continue
driver.close()

