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


driver.get("https://www.banglanews24.com/")

print(driver.title)
