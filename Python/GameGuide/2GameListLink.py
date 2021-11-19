from datetime import datetime
import os
import requests
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
        time.sleep(1)
        foldername=str(line).split("/")[-1]
        foldername=foldername.rsplit('.', 1)[0]
        if os.path.exists(foldername):
            pass
        else:
            os.mkdir(foldername)
            
        title=driver.find_element(By.XPATH,"//span[@class='big']")
        title=title.text
        
        print("Title = "+title)
        
        images=driver.find_elements(By.XPATH,"//div[@class='c-detail glzjshow_con']//img[@src]")

        for image in images:
            url=image.get_attribute('src')
            print("Image Link= "+url)
            filename=url.split("/")[-1]
            full_path=os.path.join(foldername,filename)
            response=requests.get(url)
            with open (full_path,"wb") as fh:
                fh.write(response.content)
            

            
            
            
        
        with open('2GameListLink_Log.txt', 'a', encoding="utf-8") as fp:
            fp.write("Line # "+str(count)+" "+str(line)+"\n")
            fp.write("Title = " + title)
            
            # For reading time title.read().decode('utf8')
    else:
        pass
        
time.sleep(10)   


now = datetime.now()
with open('2GameListLink_Log.txt', 'a') as fp:
    fp.write("\n*********** End Time << "+str(now) +" ***************")
    
    
            
        
 
 