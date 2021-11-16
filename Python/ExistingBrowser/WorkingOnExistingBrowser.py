from datetime import datetime
import os

import keyboard
import pyautogui
import time



x=int(input("Enter Starting Yee Old Doodles Number: "))
y=int(input("Enter Ending Yee Old Doodles Number: "))
t=int(input("Enter Page load Max wait time in seconds(like =7): "))

now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("\n\nStarted Time >> "+str(now))
    fp.write("\n")
    fp.write("Range You Selected = "+str(x)+" To "+str(y)+"\n")

opensea_page= None
opensea_page=pyautogui.locateOnScreen('opensea.png')

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
        pyautogui.keyDown('ctrl')
        pyautogui.press('l')
        pyautogui.keyUp('ctrl')
        time.sleep(.5)
        pyautogui.write('https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/'+str(x)) 
        time.sleep(.5)
        pyautogui.press('enter')
        
        owned_by= None
        l=0
        while (owned_by==None) and l<t:
            owned_by=pyautogui.locateOnScreen('owned_by.png')
            print("Still haven't load Doodle #"+str(x)+" details page. \n")
            time.sleep(1)
            l=l+1
            
        if owned_by==None:
            print("Doodles #"+str(x)+" details page cannot load tried"+str(l)+" seconds")
            now = datetime.now()
            with open('opensea_log.txt', 'a') as fp:
                fp.write("\n\n"+str(now)+" : ")
                fp.write("Doodles #"+str(x)+" details page cannot load tried"+str(l)+" seconds. Script Stop Here.")
        
        else:        
            time.sleep(3)
            price=pyautogui.locateOnScreen('current_price.png')
            if price==None:
                with open('opensea_log.txt', 'a') as fp:
                    fp.write(str(x)+" = Pending")
                    fp.write("\n")
            
                print(str(x)+" >> Pending\n")
                print("Going to Sell Page....\n")
                pyautogui.keyDown('ctrl')
                pyautogui.press('l')
                pyautogui.keyUp('ctrl')
                time.sleep(.5)
                pyautogui.write('https://opensea.io/assets/matic/0x27947e2577c21f2f74df05ae8fc376648b203eb2/'+str(x)+'/Sell')
                time.sleep(.5)
                pyautogui.press('enter')
                time.sleep(5)
        
            else:
                with open('opensea_log.txt', 'a') as fp:
                    fp.write(str(x)+" = Already Done")
                    fp.write("\n")
                print(str(x)+" >> Already Done\n")
            
            x=x+1
        
now = datetime.now()
with open('opensea_log.txt', 'a') as fp:
    fp.write("End Time << "+str(now))
    fp.write("\n")  
    
            
        
 
 