import json
from datetime import datetime
import os

import keyboard
import pyautogui
import time

x=int(input("Enter Starting Yee Old Doodles Number: "))
y=int(input("Enter Ending Yee Old Doodles Number: "))
t=int(input("Enter Page loading time in seconds(like =7): "))

now = datetime.now()
with open('json_log.txt', 'a') as fp:
    fp.write("\n\nStarted Time >> "+str(now))
    fp.write("\n")
    fp.write("Range You Selected = "+str(x)+" To "+str(y)+"\n")
    
with open('_metadata.json') as f:
   data = json.load(f)

opensea_page=pyautogui.locateOnScreen('opensea.png')


if opensea_page==None:
    print("opensea.png image cannot pointed on the browser")
else:
    time.sleep(1)
    pyautogui.click('opensea.png')
    time.sleep(t)
    
    for i in range(x,y+1):       
        print(str(x)+" >> Going to create\n")
       
        pyautogui.keyDown('ctrl')
        pyautogui.press('l')
        pyautogui.keyUp('ctrl')
        time.sleep(.5)
        pyautogui.write('https://opensea.io/asset/create')
        pyautogui.press('enter')
        time.sleep(t)
        
        pyautogui.press('tab',4)
        time.sleep(.5)
        pyautogui.press('tab',5)
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        
        time.sleep(2)
        pyautogui.write(str(x)+'.png')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        
        # Now go to the name texbox with tab click
        pyautogui.press('tab', 2)
        name=data[x-1]['name']
        pyautogui.write(name)
        print(name)
        time.sleep(1)
        
        
        # Now go to the description text box [may be two times tab click require]
        pyautogui.press('tab',3)
        description=data[x-1]['description']
        pyautogui.write(description)
        time.sleep(1)
        
        # Now go to select collection
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        
        # Now go to properties add button
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        
        #Open Window
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter', 7)
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        #Properties added popup window will be appeared
        attribute=data[x-1]['attributes']
        
        for a in range(8):   
            attribute_trait=attribute[a]['trait_type']
            attribute_value=attribute[a]['value']
        
            #start typing attribute
            pyautogui.write(attribute_trait)
            time.sleep(.3)
            pyautogui.press('tab')
            time.sleep(.3)
            pyautogui.write(attribute_value)
            time.sleep(.3)
            pyautogui.press('tab')
            time.sleep(.3)
            

        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('tab', 16)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        x=x+1
        
 