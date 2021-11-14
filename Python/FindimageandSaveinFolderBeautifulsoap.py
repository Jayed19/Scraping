import requests
from bs4 import BeautifulSoup
import os
import pandas
from requests import Session
from bs4 import BeautifulSoup as bs
from requests.api import request
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
import re




url="https://www.banglanews24.com/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

all_images=soup.find_all('img')
imgurls=[img['src'] for img in all_images]

if os.path.exists("images"):
    pass
else:
    os.mkdir('images')


for imgurl in imgurls:
    #print("\n\n"+imgurl)
    filename=imgurl.split("/")[-1]
    extension=imgurl.split(".")[-1]
    if extension in ('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif'):
        full_path=os.path.join('images',filename)
    
        if 'http' in imgurl:
        
            response=requests.get(imgurl)
        
            with open (full_path,"wb") as fh:
                fh.write(response.content)
                

    else:
        pass
    
            

   
 



