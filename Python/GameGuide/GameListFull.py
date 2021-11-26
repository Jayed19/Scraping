from datetime import datetime
import os
from subprocess import getstatusoutput
import requests
import keyboard
import pyautogui
import time
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
import getpass

print("There are 3 Modes You can start your script.")
print("0 For start from the very begining. Collect All URL.\n1 For Collect All URL Done. Now Start from First List.\n2 For Script you want to start a specific Line of the collecting all URL List.")
mode=int(input("Enter Your Mode (Press 0 or 1 or 2): "))


if mode not in (0,1,2):
    print("Your Mode Selection is wrong. Select 0 or 1 or 2.")
    with open('Log.txt', 'a') as fp:
        fp.write("\nYour Mode Selection is wrong. Select 0 or 1 or 2.")
    sys.exit()
    
if mode==0:
    #Mode: 0 >> Collect All URL from Main Page
    url=str(input("Enter Main URL: "))

global specific_url
if mode==2:
    specific_url=str(input("Type Specific URL from where you want to start: "))
 
un=str(input("Enter your wordpress User Name:"))
pwd=getpass.getpass("Enter Password: ")


opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.set_page_load_timeout(300)


now = datetime.now()
with open('log.txt', 'a') as fp:
    fp.write("\n********** Started Time "+str(now)+" ****************")
    

if mode==0:

    # For Finding all link

    start_time = datetime.now()
    #driver.get("https://gl.ali213.net/z/58479/")
    
    driver.get(url)
    end_time = datetime.now()

    print('Duration For Loading Main Page: {}'.format(end_time - start_time))
    with open('log.txt', 'a') as fp:
        fp.write('\nDuration For Loading Main Page: {}'.format(end_time - start_time))

    time.sleep(10)

    #lists=driver.find_elements(By.XPATH,"//div[@class='glzj_infob_rnew clearFloat']//a[contains(@href,'')]")
    # Fix Issue for different type pages
    lists=driver.find_elements(By.XPATH,"//div[@class='glzj_infob_rnew_onel']/a[@href]")
    
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
    
    now = datetime.now()
    with open('log.txt', 'a') as fp:
        fp.write("\nEnd Time of Collecting All URLS>> "+str(now))
        
    mode=1
# End of All URL collection


#Starting Mode 1
global starting_url
if mode==1:
    # Starting individual page loading
    file1 = open('allhref.txt', 'r+')
    lines = file1.readlines()
    starting_url=lines[0]
    print("Starting URL: "+starting_url)
   
    with open('log.txt', 'a') as fp:
        fp.write("\nStarting URL: "+starting_url)
    if len(starting_url)==0:
        sys.exit()
    
if mode==2:
       
    file1 = open('allhref.txt', 'r+')
    lines = file1.readlines()
    if specific_url+"\n" in lines:
        print("Specific URL Found")
        with open('Log.txt', 'a') as fp:
            fp.write("\nSpecific URL: "+specific_url)
        starting_url=specific_url+"\n"

    
    else:
        print("Specific URL not Found") 
        with open('Log.txt', 'a') as fp:
            fp.write("\nSpecific URL not Found"+specific_url) 
        sys.exit()
    


global starting_number
with open('allhref.txt') as fp:
    for num, line in enumerate(fp,1):
        if starting_url in line:
            print('Starting URL Found in Line Number# '+str(num))
            starting_number=num
            

print("Got the Starting Line Number#"+str(starting_number))        
with open('Log.txt', 'a') as fp:
    fp.write("\nGot the Starting Line Number# "+str(starting_number))  


  
loginflag=0
with open('allhref.txt') as fp:
    for num, line in enumerate(fp,1):
        if num>=starting_number: 
            print("Continue Line # "+str(num))
            print("URL"+line)
            driver.get(line)
            time.sleep(5)
            with open('Log.txt', 'a') as fp:
                fp.write("\nContinue Line # "+str(num))
                fp.write("\nURL"+line)
        
            #Scrap Starting 
            foldername=str(line).split("/")[-1]
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

            # Fix Issue Title remove category with bracket
            removal_text='《'+category+'》'
            title=title.replace(removal_text, "", 1)
            print("Issue Fix Title="+title)
                    
                    #Scrap article
            article=driver.find_element(By.XPATH,"//div[@class='c-detail glzjshow_con']").text
            print("articale = "+ article)
            #Fix issue on articles
            removal_articles=driver.find_element(By.XPATH,"//p//span[@class='n_show_g']").text
            print("articles remove part = "+removal_articles)
            removal_articles2=driver.find_element(By.XPATH,"//a[@class='morezjjump']").text
            print("articles remove part2 = "+removal_articles2)

            article = "".join(article.rsplit(removal_articles, 1))
            article = "".join(article.rsplit(removal_articles2, 1))
            print("Article Issue Fix= "+article)

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

                time.sleep(1)
            
            time.sleep(2)



            #Translation Start using googletrans package

            #pip install pip install googletrans==3.1.0a0
            from googletrans import Translator
            translator = Translator()

            #Translate Cetegory
            chinese_traditional=translator.translate(category, dest='zh-tw')
            category=chinese_traditional.text
            print("Category Traditional= " + category)

            #Translate Title
            chinese_traditional=translator.translate(title, dest='zh-tw')
            title=chinese_traditional.text
            print("Title Traditional= " + title)

            #Translate article
            chinese_traditional=translator.translate(article, dest='zh-tw')
            article=chinese_traditional.text
            print("article Traditional= " + article)

            #Translate metadata
            chinese_traditional=translator.translate(metadata, dest='zh-tw')
            metadata=chinese_traditional.text
            print("metadata Traditional= " + metadata)

            '''
            #Transalation By Browsing

            driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
            driver.set_page_load_timeout(300)

            time.sleep(2)
            Translator_text="https://translate.google.com/?sl=zh-CN&tl=zh-TW&text="+category+"&op=translate"    
            driver.get(Translator_text)
            time.sleep(3)
            print("Category in Chinese Lang: "+ category)
            category = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text
            print("Category in Traditional Language " + category)

            time.sleep(5)
            '''

            #WordPress Login and Post Page
            if loginflag==0:
                time.sleep(1)
                driver.get("https://gameguide.best/wp-admin")
                time.sleep(3)
                user=driver.find_element(By.ID,'user_login')
                user.send_keys(un)
                password=driver.find_element(By.ID,'user_pass')
                password.send_keys(pwd)

                time.sleep(1)
                login=driver.find_element(By.ID,'wp-submit')
                login.click()
                time.sleep(6)
            
            
            loginflag=1
            time.sleep(2)
            driver.get("https://gameguide.best/wp-admin/post-new.php")
            time.sleep(6)

            driver.find_element(By.NAME,'post_title').send_keys(title)
            time.sleep(2)

            # Browse images
            button=driver.find_element(By.ID,"insert-media-button")
            button.click()
            time.sleep(4)

            uploadmenu=driver.find_element(By.ID,'menu-item-upload')
            ActionChains(driver).move_to_element(uploadmenu).click(uploadmenu).perform()
            time.sleep(3)
            
            

            select=driver.find_element(By.ID,'__wp-uploader-id-1')
            ActionChains(driver).move_to_element(select).click(select).perform()

            time.sleep(4)
            pyautogui.write(os.getcwd())
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write(foldername)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.keyDown('shift')
            pyautogui.press('tab') 
            pyautogui.keyUp('shift')
            time.sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.press('a') 
            pyautogui.keyUp('ctrl')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(12)

            addtopost=driver.find_element(By.XPATH,"//button[@class='button media-button button-primary button-large media-button-insert']")
            ActionChains(driver).move_to_element(addtopost).click(addtopost).perform()
            time.sleep(10)

            #Select iFrame
            element = driver.find_element(By.ID,'content_ifr')

            #Switch to iFrame
            driver.switch_to.frame(element)

            #Query document for the ID that you're looking for
            queryElement = driver.find_element(By.ID,'tinymce')

            #Send key to the ID
            queryElement.send_keys(article)

            #Switch back to default content from iFrame
            driver.switch_to.default_content()

            time.sleep(3)


            element3=driver.find_element(By.ID,"category-add-toggle")
            b=ActionChains(driver).move_to_element(element3).click(element3).perform()
            time.sleep(2)
            driver.switch_to.active_element.send_keys(category)

            time.sleep(3)


            #driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(.your_css_selector))
            element2=driver.find_element(By.XPATH,"//div[@class='sc-hOGjNT sc-gUQueJ sc-gJbFMZ ghXohb eSdaFP bSTeTo yst-replacevar__editor']")
            a=ActionChains(driver).move_to_element(element2).click(element2).perform()
            time.sleep(2)
            driver.switch_to.active_element.send_keys(metadata)
            time.sleep(4)
            #Scroll go to the Top of the Page
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(3)
            publish=driver.find_element(By.ID,'publish')
            publish.click()
            time.sleep(4)



