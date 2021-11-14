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
from selenium.common.exceptions import NoSuchElementException




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(800, 700)

driver.get("https://opensea.io/collection/yeeolddoodles")




a = ActionChains(driver)
my_xpath = "//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 iOJWKT jYqxGr ksFzlZ']/div[@class='Blockreact__Block-sc-1xf18x6-0 dBFmez AssetCardFooter--trading-annotations']"
firstelement=driver.find_element(By.XPATH,my_xpath)
a.move_to_element(firstelement).perform()

ignorexpath="//div[@class='AssetCardFooter--price']"
ignoringelement=driver.find_element(By.XPATH,ignorexpath)

clickpath="//img[@class='Image--image']"
clickelement=driver.find_element(By.XPATH,clickpath)

x=1
for x in range(50):
    
        #
    x=x+1
    print("\ncount"+str(x))
    
    time.sleep(.5)
    ignorexpath="//div[@class='AssetCardFooter--price']"
    
    try:
        driver.find_element(By.XPATH,ignorexpath)
        driver.execute_script("window.scrollTo(0,window.scrollY + 522)")
    except NoSuchElementException:
        time.sleep(3)
        clickpath="//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 iOJWKT jYqxGr ksFzlZ']/div[@class='Blockreact__Block-sc-1xf18x6-0 dBFmez AssetCardFooter--trading-annotations']"
        clickelement=driver.find_element(By.XPATH,clickpath)
        driver.execute_script("arguments[0].click();", clickelement)
        time.sleep(15)
        sellpath="\\a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 jxgnwF kCijbX OrderManager--second-button']"
        
        sellelement=driver.find_element(By.XPATH,sellpath)
        
        time.sleep(3)
        driver.execute_script("arguments[0].click();", sellelement)
        time.sleep(15)
        
    
    
   
    



