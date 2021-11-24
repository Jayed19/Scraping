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
driver.close()
   
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


#Transalation By Browsing
'''
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
opts=webdriver.ChromeOptions()
opts.headless=False

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
driver.set_page_load_timeout(300)


driver.get("https://gameguide.best/wp-admin")
time.sleep(3)
user=driver.find_element(By.ID,'user_login')
user.send_keys("test1234")
password=driver.find_element(By.ID,'user_pass')
password.send_keys("6pC0dL)VV#vhm$HBzUr4eHu1")

time.sleep(1)
password=driver.find_element(By.ID,'wp-submit')
password.click()
time.sleep(6)

driver.get("https://gameguide.best/wp-admin/post-new.php")
time.sleep(6)

driver.find_element(By.NAME,'post_title').send_keys(title)
time.sleep(1)


#driver.find_element(By.XPATH,"//div[@class='sc-hOGjNT sc-gUQueJ sc-gJbFMZ ghXohb eSdaFP bSTeTo yst-replacevar__editor']").send_keys(metadata)
time.sleep(3)



    
        
 
 