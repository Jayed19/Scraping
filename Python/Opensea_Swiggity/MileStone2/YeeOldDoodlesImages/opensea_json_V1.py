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
    x=x-1
    for i in range(x,y+1):       
        print(str(x)+" >> Going to create\n")
       
        pyautogui.keyDown('ctrl')
        pyautogui.press('l')
        pyautogui.keyUp('ctrl')
        time.sleep(.5)
        pyautogui.write('https://opensea.io/asset/create')
        pyautogui.press('enter')
        time.sleep(t)
        
        # mouse click on the photo. Have to place your own photo icon image in photo.png
        photo_page=pyautogui.locateOnScreen('photo.png')
        if photo_page==None:
               print("Create page is not loaded yet")
        else:
               #click on the photo icon
               time.sleep(1)
               pyautogui.click('photo.png')
               
               #type image number in the textbox
               time.sleep(2)
               pyautogui.write(str(x)+'.png')
               
               # press enter after photo selection done
               time.sleep(1)
               pyautogui.press('enter')
               time.sleep(1)
               
               # Now go to the name texbox with tab click
               pyautogui.press('tab')
               time.sleep(.5)
               name=data[x]['name']
               pyautogui.write(name)
               time.sleep(1)
               
               # Now go to the description text box [may be two times tab click require]
               pyautogui.press('tab',2)
               description=data[x]['description']
               pyautogui.write(description)
               time.sleep(1)
               
               # Now go to select collection
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press("down")
               time.sleep(.5)
               pyautogui.press('enter')
               time.sleep(1)
               
               # Now go to properties add button
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('enter')
               time.sleep(2)
               
               #Properties added popup window will be appeared
               attribute=data[x]['attributes']
                        
               # Loop for typing 8 attributes
               
               for a in range(8):   
                  attribute_trait=attribute[a]['trait_type']
                  attribute_value=attribute[a]['value']
               
                  #start typing attribute
                  pyautogui.write(attribute_trait)
                  time.sleep(.5)
                  pyautogui.press('tab')
                  time.sleep(.5)
                  pyautogui.write(attribute_value)
                  time.sleep(.5)
                  pyautogui.press('tab')
                  time.sleep(.5)
                  pyautogui.press('enter')
                  time.sleep(.5)
                  
               
               
               # After completing 8 properties go to Save button. may require two times Tab
               time.sleep(1)
               pyautogui.press('tab',2)
               time.sleep(.5)
               pyautogui.press('enter')
               time.sleep(2)
               
               # For click on the create button may require 5 times Tab. Add accordingly
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('tab')
               time.sleep(.5)
               pyautogui.press('enter')
               time.sleep(t)
               
               #Write log for this doodles
               with open('json_log.txt', 'a') as fp:
                  fp.write("\n You created Doodles# "+str(x))
                  
               
               # Hope Enter key will close the popup and back to the Opensea Home page
               pyautogui.press('enter')
               time.sleep(3)
               
               #Again go to the home page 
               pyautogui.click('opensea.png')
               time.sleep(t)
               
               
                  
               x=x+1
               
now = datetime.now()
with open('json_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")  
               
      