from datetime import datetime
import os

import keyboard
import pyautogui
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



now = datetime.now()
with open('1gamelist_log.txt', 'a') as fp:
    fp.write("\n\n********** Started Time >> "+str(now)+" ****************")



opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.set_page_load_timeout(300)

# For Finding all link

start_time = datetime.now()
driver.get("https://gl.ali213.net/z/58479/")
end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))
with open('1gamelist_log.txt', 'a') as fp:
    fp.write('\nDuration: {}'.format(end_time - start_time))

time.sleep(10)

lists=driver.find_elements(By.XPATH,"//div[@class='glzj_infob_rnew clearFloat']//a[contains(@href,'')]")

if os.path.exists("allhref.txt"):
    os.remove("allhref.txt")
i=1
for list in lists:
   
    print("\n"+str(i)+" = "+list.get_attribute("href"))
    with open('1gamelist_log.txt', 'a') as fp:
        fp.write("\n"+str(i)+" = "+list.get_attribute("href"))
        

    time.sleep(.1)        
    with open('allhref.txt', 'a') as fp:
        fp.write(list.get_attribute("href")+"\n")
    i=i+1
 
