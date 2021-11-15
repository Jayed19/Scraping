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
        
    x=x+1
    
    
now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")   
        
        
    
    



'''

a = ActionChains(driver)
my_xpath = "//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 iOJWKT jYqxGr ksFzlZ']/div[@class='Blockreact__Block-sc-1xf18x6-0 dBFmez AssetCardFooter--trading-annotations']"
firstelement=driver.find_element(By.XPATH,my_xpath)
a.move_to_element(firstelement).perform()

ignorexpath="//div[@class='AssetCardFooter--price']"
ignoringelement=driver.find_element(By.XPATH,ignorexpath)

clickpath="//img[@class='Image--image']"
clickelement=driver.find_element(By.XPATH,clickpath)
'''


'''
x=1
for x in range(50):
    

    x=x+1
    print("\ncount"+str(x))
    
    #Comment out done section
    
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
 '''       
 
 # Doing with CSV and pandas

'''  
import pandas
df = pandas.DataFrame()
saleList =[]
skipList=[]
x=1
for x in range(100):
    

    x=x+1
    print("\ncount"+str(x))
    
    #Comment out done section
    
    
    ignorexpath="//div[@class='AssetCardFooter--price']"
    anchorxpath="//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']"
    try:
       
        driver.find_element(By.XPATH,ignorexpath)
        link=driver.find_element(By.XPATH,anchorxpath).get_attribute('href')
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,anchorxpath))).get_attribute("href")
                                    
        
        
        skipList.append(link)
        print("Link = "+link)
        driver.execute_script("window.scrollTo(0,window.scrollY + 522)")
        time.sleep(1)
    except NoSuchElementException:
        
        
        link=driver.find_element(By.XPATH,anchorxpath).get_attribute('href')
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,anchorxpath))).get_attribute("href")
        saleList.append(link)
        print("Link = "+link)
        driver.execute_script("window.scrollTo(0,window.scrollY + 522)")
        time.sleep(1)

df["Sale Link"]=pandas.Series(saleList)




df.to_csv('test.csv', index=True)

'''     
'''
# Writ in normal txt file

x=1
for x in range(10000):
    

    x=x+1
    print("\ncount"+str(x))
    
    #Comment out done section
    
    
    ignorexpath="//div[@class='AssetCardFooter--price']"
    anchorxpath="//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']"
    try:
       
        driver.find_element(By.XPATH,ignorexpath)
        link=driver.find_element(By.XPATH,anchorxpath).get_attribute('href')
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,anchorxpath))).get_attribute("href")
                                    

        print("Link = "+link)
        driver.execute_script("window.scrollTo(0,window.scrollY + 522)")
        time.sleep(1)
    except NoSuchElementException:
        
        
        link=driver.find_element(By.XPATH,anchorxpath).get_attribute('href')
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,anchorxpath))).get_attribute("href")
            
        with open('link.txt', 'a') as fp:
            fp.write(link)
            fp.write("\n")
      
        print("Link = "+link)
        driver.execute_script("window.scrollTo(0,window.scrollY + 522)")
        time.sleep(1)

'''