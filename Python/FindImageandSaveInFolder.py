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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("http://shuishuto.xyz/")

#Write Full Page Source by Selenium Web Driver
content=driver.page_source

if os.path.exists("page"):
    pass
else:
    os.mkdir('page')
    
    
with open('page/page.html', 'w', encoding="utf-8") as fp:
    fp.write(content)
# Write only visible text in selenium web driver

allvisibletext=driver.find_element_by_tag_name('body').text
with open('page/page.txt', 'w', encoding="utf-8") as fp:
    fp.write(allvisibletext)

time.sleep(5)
# Write all Product Info



a = ActionChains(driver)
m=driver.find_element_by_xpath("//div[starts-with(@class,'col-lg-4 col-md-6 portfolio-item')]/div[@class='portfolio-info']")
a.move_to_element(m).perform()
print(m.text)


m=driver.find_elements_by_xpath("//div[starts-with(@class,'col-lg-4 col-md-6 portfolio-item')]/div[@class='portfolio-info']")

ini=0

for l in m:
    a.move_to_element_with_offset(l,5,5).perform()
    print(l.text)
    
    with open('page/product.txt', 'a', encoding="utf-8") as fp:
        fp.write("\n"+"Product Number "+str(ini)+"\n")
        fp.write(".......................\n")
        fp.write(l.text)
    
    
    ini=ini+1
    if (ini%3)==0:
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,window.scrollY + 400)")
        
        time.sleep(3)
    else:
        pass