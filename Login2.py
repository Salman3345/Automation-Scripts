from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import urllib.parse
import config as cnfg
url = cnfg.url
stageurl = cnfg.stageurl
path = "/en/trade/login"
path_2 = "/en/trade/BTC-USDT"
path_3 = "/en/trade/account/settings"

def test(User,Pas):
    driver = webdriver.Chrome()
    driver.get(urllib.parse.urljoin(stageurl, path))
    wait = WebDriverWait(driver, 10)
    E = driver.find_element_by_id("email")
    E.send_keys(User)
    p = driver.find_element_by_id("password")
    p.send_keys(Pas)
    time.sleep(2)
    driver.find_element_by_id("loginForm").click()
    wait.until(EC.url_to_be(urllib.parse.urljoin(stageurl, path_2)))
    driver.get(urllib.parse.urljoin(stageurl, path_3))

with open('Test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter =",")
    i = 0
    
    for row in readCSV:
        
        if i > 0:
         if row[2] in ['ValidLoginCredentials']:
            User=row[0]
            Pas=row[1]
            test(User,Pas)
            print("Login Test: Pass")
            
        elif row[2] in ['InvalidEmailCredentials']:
               User=row[0]
               Pas=row[1]
               test(User,Pas)
               
        i=i+1