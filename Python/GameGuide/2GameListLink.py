from datetime import datetime
import os

import keyboard
import pyautogui
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


x=int(input("Enter Starting Serial of the loop: "))
y=int(input("Enter Ending Ending Serial of the loop: "))


now = datetime.now()
with open('2GameListLink_Log.txt', 'a') as fp:
    fp.write("\n\n********** Started Time >> "+str(now)+" ****************")
    fp.write("\nRange You Selected = "+str(x)+" To "+str(y)+"\n")


opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.set_page_load_timeout(300)

# Starting individual page loading
file1 = open('allhref.txt', 'r')
lines = file1.readlines()

count=0
for line in lines:
    count=count+1
    if count>=x and count<=y:
        print("Line # "+str(count)+" "+str(line)+"\n")
        driver.get(line)
        with open('2GameListLink_Log.txt', 'a') as fp:
            fp.write("Line # "+str(count)+" "+str(line)+"\n")
    else:
        print(str(count)+"Not in range")
        
time.sleep(10)   


now = datetime.now()
with open('2GameListLink_Log.txt', 'a') as fp:
    fp.write("\n*********** End Time << "+str(now) +" ***************")
    
    
            
        
 
 