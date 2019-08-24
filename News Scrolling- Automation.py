# Author Venkatesh Thirunagiri
# How it Works :
#                it opens a sepecified News Website then it Atomatically Scroll Downs until it reaches to end 
#                Meanwhile it give some time to read HeadLines

from selenium import webdriver
import time
driver=webdriver.Chrome("Chrome Webdriver Path")
driver.get("https://www.bbc.com/news")
driver.maximize_window()
height=driver.execute_script("return document.body.scrollHeight")
x,y=0,200
while y < height:
    driver.execute_script("window.scrollTo({0},{1})".format(x,y))
    x=y
    y = y+300
    time.sleep(5)  # it sleeps 5 seconds to get in touch with the Headlines
    continue
driver.close()  
