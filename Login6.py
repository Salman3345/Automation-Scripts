from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import urllib.parse
import config as cnfg
url = cnfg.url
stageurl = cnfg.url
path ="/en/trade/login"

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
    time.sleep(4)
    if wait.until(EC.title_contains(("Login Now"))):
        print("Login Test : Pass") 
    else:
        
        print("Login Test : Fail")  

with open('Test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter =",")
    i = 0
    
    for row in readCSV:
        
        if i > 0:
         if row[2] in ['CredentialsBlocked']:
            User=row[0]
            Pas=row[1]
            test(User,Pas)
            
            
        elif row[2] in ['InvalidEmailCredentials']:
               User=row[0]
               Pas=row[1]
               test(User,Pas)
               
        i=i+1