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


opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)


driver.get("https://www.banglanews24.com/")

print(driver.title)

if os.path.exists("images"):
    pass
else:
    os.mkdir('images')

all_images=driver.find_elements(By.XPATH,"//img[@src]")



for img in all_images:
    url=img.get_attribute('src')
    print("URL= "+url)
    filename=url.split("/")[-1]
    print("FileName= "+filename)
    
    full_path=os.path.join('images',filename)
    response=requests.get(url)
    with open (full_path,"wb") as fh:
        fh.write(response.content)