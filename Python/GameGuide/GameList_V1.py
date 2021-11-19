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
t=int(input("Enter Page Maximum loading time in seconds(like =7): "))

now = datetime.now()
with open('gamelist_log.txt', 'a') as fp:
    fp.write("\n\nStarted Time >> "+str(now))
    fp.write("\nRange You Selected = "+str(x)+" To "+str(y)+"\n")


opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.implicitly_wait(300)

start_time = datetime.now()
driver.get("https://gl.ali213.net/z/58479/")
end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))
with open('gamelist_log.txt', 'a') as fp:
    fp.write('\nDuration: {}'.format(end_time - start_time))


lists=driver.find_elements(By.XPATH,"//div[@class='glzj_infob_rnew clearFloat']/div[@class='glzj_infob_rnew_onel']/a[@href]")


i=1
for list in lists:
   
    print("\n"+str(i)+" = "+list.text)
    with open('gamelist_log.txt', 'a') as fp:
        fp.write("\n"+str(i)+" = "+list.text)



'''
# dynamic waiting
opensea_page=None
l=0
while (opensea_page==None) and l<t:
    
    opensea_page=pyautogui.locateOnScreen('opensea.png')
    print("Still haven't found the opensea website visible in the screen...\n")
    time.sleep(1)
    l=l+1


if opensea_page==None:
    print("Opensea website is not visible on the screen tried "+str(l)+" seconds")
    now = datetime.now()
    with open('opensea_log.txt', 'a') as fp:
        fp.write("\n\n"+str(now)+" : ")
        fp.write("Opensea website is not visible on the screen tried "+str(l)+" seconds")
        
else:
    print("\nOpensea website is visible.")
    time.sleep(1)
    pyautogui.click('opensea.png')
    time.sleep(2)
    for i in range(x,y+1):       
        print(str(x)+" >> Pending\n")
        print("Going to Sell Page....\n")
        pyautogui.keyDown('ctrl')
        pyautogui.press('l')
        pyautogui.keyUp('ctrl')
        time.sleep(.5)
        pyautogui.write('https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/'+str(x)+'/Sell',interval=.05)
        time.sleep(.5)
        pyautogui.press('enter')
        
        # Dynamic wait added  
        price= None
        l=0
        while (price==None) and l<t:
            owned_by=pyautogui.locateOnScreen('price.png')
            print("Still haven't load Doodle #"+str(x)+" Sell page. \n")
            time.sleep(1)
            l=l+1
            
        if price==None:
            print("Doodles #"+str(x)+" Sell page cannot load tried"+str(l)+" seconds")
            print("Stop Script")
            now = datetime.now()
            with open('opensea_log.txt', 'a') as fp:
                fp.write("\n\n"+str(now)+" : ")
                fp.write("Doodles #"+str(x)+" Sell page cannot load tried"+str(l)+" seconds. Script Stop Here.")
            break
        
        else:
            
        
            time.sleep(2)
            pyautogui.write('0.05')
            time.sleep(.5)
            pyautogui.press('enter')
            
            # dynamic wait for Sign button
             
            sign= None
            s=0
            while (sign==None) and s<t:
                sign=pyautogui.locateOnScreen('sign_button.png')
                print("Still haven't load Doodle #"+str(x)+" Sign page. \n")
                time.sleep(1)
                s=s+1
                
            if sign==None:
                print("Doodles #"+str(x)+" Sign page cannot load tried"+str(l)+" seconds")
                print("Stop Script")
                now = datetime.now()
                with open('opensea_log.txt', 'a') as fp:
                    fp.write("\n\n"+str(now)+" : ")
                    fp.write("Doodles #"+str(x)+" Sign page cannot load tried"+str(l)+" seconds. Script Stop Here.")
                break
        
            
            
            
            pyautogui.press('tab')
            time.sleep(2)
            pyautogui.press('tab')
            time.sleep(2)
            pyautogui.press('enter')
            
            # dynamic wait for going to sign
                                    
            going_sign= None
            g=0
            while (going_sign==None) and g<t:
                going_sign=pyautogui.locateOnScreen('going_sign.png')
                print("Still haven't load Doodle #"+str(x)+" Going Sign page. \n")
                time.sleep(1)
                g=g+1
                
            if going_sign==None:
                print("Doodles #"+str(x)+" going Sign page cannot load tried"+str(l)+" seconds")
                print("Stop Script")
                now = datetime.now()
                with open('opensea_log.txt', 'a') as fp:
                    fp.write("\n\n"+str(now)+" : ")
                    fp.write("Doodles #"+str(x)+" going Sign page cannot load tried"+str(l)+" seconds. Script Stop Here.")
                break
            
            
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('enter')
            
            
            # dynamic wait for Last Page         
            last_screen= None
            f=0
            while (last_screen==None) and f<t:
                last_screen=pyautogui.locateOnScreen('last_screen.png')
                print("Still haven't load Doodle #"+str(x)+" Last page. \n")
                time.sleep(1)
                f=f+1
                
            if last_screen==None:
                print("Doodles #"+str(x)+" Last page cannot load tried"+str(l)+" seconds")
                print("Stop Script")
                now = datetime.now()
                with open('opensea_log.txt', 'a') as fp:
                    fp.write("\n\n"+str(now)+" : ")
                    fp.write("Doodles #"+str(x)+" Last page cannot load tried"+str(l)+" seconds. Script Stop Here.")
                break


            
            x=x+1

'''       
now = datetime.now()
with open('gamelist_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")  
    
            
        
 
 