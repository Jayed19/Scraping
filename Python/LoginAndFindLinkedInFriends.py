import requests
from bs4 import BeautifulSoup
import os
import pandas
from requests import Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import getpass
from selenium.webdriver.common.keys import Keys
import pprint
from webdriver_manager.chrome import ChromeDriverManager
import time



#userid=str(input("Enter email address: "))
userid='jayed19@gmail.com'
password=getpass.getpass("Enter Password")


driver = webdriver.Chrome(ChromeDriverManager().install())
#chrome_path='./chromedriver'
#driver=webdriver.Chrome(chrome_path)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

driver.implicitly_wait(10)
driver.find_element_by_name('session_key').send_keys(userid)
driver.find_element_by_name('session_password').send_keys(password)
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

driver.get("https://www.linkedin.com/in/md-sanaul-islam-39408935/")
time.sleep(5)

# //div[@class='mt2 relative']   this is for finding by class name exactly
print("Full Section Print")
conn=driver.find_element_by_xpath("//div[@class='mt2 relative']")
print(conn.text)
# /div[starts-with(@class,'pv-text-details__left-panel')] this is for findout by partial class name
print("Only Basic Info Print")
con2=driver.find_element_by_xpath("//div[@class='mt2 relative']/div[starts-with(@class,'pv-text-details__left-panel')]")
print(con2.text)

# this is for finding the name only
print("Only Name Print")
con3=driver.find_element_by_xpath("//h1[starts-with(@class,'text-heading-xlarge inline t-24 v-align-middle')]")
print(con3.text)


    
    

