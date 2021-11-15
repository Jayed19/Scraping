import requests
import os
from requests import Session
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime



opts=webdriver.ChromeOptions()
opts.headless=False

global x
x=int(input("Enter Starting Yee Old Doodles Number: "))
y=int(input("Enter Ending Yee Old Doodles Number: "))



driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)

driver.implicitly_wait(10)
now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("\n\nStarted Time >> "+str(now))
    fp.write("\n")
    fp.write("Range You Selected = "+str(x)+" To "+str(y)+"\n")
        


for i in range(x,y+1):
 
    
    driver.get("https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/"+str(x))
    time.sleep(2)
    
    ignorexpath="//div[@class='TradeStation--price-container']"
    
    


    try:
        ignoringelement=driver.find_element(By.XPATH,ignorexpath)
        with open('opensea_log.txt', 'a') as fp:
            fp.write(str(x)+" = Already Done")
            fp.write("\n")
        print(str(x)+" >> Already Done\n")
        
    except NoSuchElementException:
        with open('opensea_log.txt', 'a') as fp:
            fp.write(str(x)+" = Pending")
            fp.write("\n")
        
        print(str(x)+" >> Pending\n")
        print("Going to Sell Page....\n")
        driver.get("https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/"+str(x)+"/Sell")
        time.sleep(2)
        
    x=x+1
    
    
now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")   
        
        
    
