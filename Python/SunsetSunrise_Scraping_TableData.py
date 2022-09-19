import requests
from bs4 import BeautifulSoup
import os
import pandas
from requests import Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import getpass
from selenium.webdriver.common.keys import Keys
import pprint
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(ChromeDriverManager().install())

Month='8'
Year='2022'
Branch='chittagong'
BranchCode='0008'
url="https://www.timeanddate.com/sun/bangladesh/"+Branch+"?month="+Month+"&year="+Year
driver.get(url)
FileName=Branch+"_"+Year+"_"+Month+"_SunRise_SunSet.xls"
#Write Full Page Source by Selenium Web Driver
content=driver.page_source


if os.path.exists("page"):
    pass
else:
    os.mkdir('page')
    
    

a = ActionChains(driver)


table_trs = driver.find_elements(By.XPATH, "//*[@id='as-monthsun']/tbody/tr")
value_list = []
if len(Month)==1:
    MonthCode='0'+Month

from datetime import datetime, timedelta

d = datetime.today() - timedelta(hours=6, minutes=00)

time=d.strftime('%H:%M')

for row in table_trs:
    dayNumber=row.find_elements(By.TAG_NAME, "th")[0].text
    if len(dayNumber)==1:
        day="0"+dayNumber
    date=Year+"-"+MonthCode+"-"+day
    #2022-09-19 23:46:25.266333
    



    sunrise=row.find_elements(By.TAG_NAME, "td")[0].text
    sunrise = sunrise.replace("↑", "")
    sunrise=sunrise.strip()
    #print(datetime.strptime(date+" "+sunrise, '%y-%m-%d %H:%M'))
    sunrise=datetime.strptime(date+" "+sunrise, '%Y-%m-%d %H:%M') - timedelta(hours=6, minutes=00)
    sunrise=sunrise.strftime('%H:%M')


    sunset=row.find_elements(By.TAG_NAME, "td")[1].text
    sunset = sunset.replace("↑", "")
    sunset=sunset.strip()
    sunset=datetime.strptime(date+" "+sunset, '%Y-%m-%d %H:%M')  - timedelta(hours=6, minutes=00)
    sunset=sunset.strftime('%H:%M')

    with open('page/'+FileName, 'a', encoding="utf-8") as fp:
        fp.write(date+"\t"+sunrise+"\t"+sunset+"\t"+BranchCode)
        fp.write("\n")

