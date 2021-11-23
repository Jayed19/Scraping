from datetime import datetime
import os
import requests
import keyboard
import pyautogui
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.common.keys import Keys
from googletrans import Translator

url=str(input("Enter URL: "))



now = datetime.now()
with open('2GameListLink_Log.txt', 'a') as fp:
    fp.write("\n\n********** Started Time >> "+str(now)+" ****************")
    fp.write("\nYour given URL = "+str(url))


opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.set_page_load_timeout(300)


driver.get(url)
time.sleep(5)
foldername=str(url).split("/")[-1]
foldername=foldername.rsplit('.', 1)[0]

if os.path.exists(foldername):
    pass
else:
    os.mkdir(foldername)
            
        # Scrap Title
title=driver.find_element(By.XPATH,"//span[@class='big']")
title=title.text
print("Title = "+title)
 
 
        # Scrap Category
category=title[title.index('《')+len('》'):title.index('》')]
print("Category = "+category)
        
        #Scrap article
article=driver.find_element(By.XPATH,"//div[@class='c-detail glzjshow_con']").text
print("articale = "+ article)

#Metadata
metadata=article.replace(category, "", 1)
metadata=metadata[0:155]
print("metadata = "+metadata)
        

images=driver.find_elements(By.XPATH,"//div[@class='c-detail glzjshow_con']//img[@src]")

for image in images:
    url=image.get_attribute('src')
    print("Image Link= "+url)
    filename=url.split("/")[-1]
    full_path=os.path.join(foldername,filename)
    response=requests.get(url)
    with open (full_path,"wb") as fh:
        fh.write(response.content)

    time.sleep(2)
   

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')  
time.sleep(2)
Translator_text="https://translate.google.com/?sl=zh-CN&tl=zh-TW&text="+category+"&op=translate"    
driver.get(Translator_text)

category = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text
print(category)

time.sleep(2)



    
        
 
 