from datetime import datetime
import os

import keyboard
import pyautogui
import time



x=int(input("Enter Starting Yee Old Doodles Number: "))
y=int(input("Enter Ending Yee Old Doodles Number: "))
t=int(input("Enter Page loading time in seconds(like =7): "))

now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("\n\nStarted Time >> "+str(now))
    fp.write("\n")
    fp.write("Range You Selected = "+str(x)+" To "+str(y)+"\n")

opensea_page=pyautogui.locateOnScreen('opensea.png')


if opensea_page==None:
    print("opensea.png image cannot pointed on the browser")
else:
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
        pyautogui.write('https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/'+str(x)+'/Sell')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(t)
        pyautogui.write('0.05')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(6)
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(6)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(6)


        
        x=x+1
        
now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")  
    
            
        
 
 