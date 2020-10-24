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
path = "/en/trade/signup"

def signup(User,Pas):
    driver = webdriver.Chrome()
    driver.get(urllib.parse.urljoin(stageurl, path))
    wait = WebDriverWait(driver, 10)
    E = driver.find_element_by_id("email")
    E.send_keys(User)
    p = driver.find_element_by_id("password")
    p.send_keys(Pas)
    p1 = driver.find_element_by_id("retype-password")
    p1.send_keys(Pas)
    time.sleep(3)
    # driver.find_element_by_class_name("recaptcha-checkbox").click()
    # driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span").clcik()
    driver.find_element_by_id("recaptcha-anchor").click()
    time.sleep(3)
    driver.find_element_by_id("mat-checkbox-1").click()
    time.sleep(2)
    driver.find_element_by_id("signupForm").click()
    time.sleep(2)
    if wait.until(EC.title_contains(("Signup Now"))):
        print("Signup Test : Pass") 
    else:
        
        print("Signup Test : Fail")    

with open('Test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter =",")
    i = 0
    
    for row in readCSV:
        
        if i > 0:
         if row[2] in ['InvalidEmailCredentials']:
            User=row[0]
            Pas=row[1]
            signup(User,Pas)
       
            
        elif row[2] in ['CredentialsNotRegistered']:
               User=row[0]
               Pas=row[1]
               signup(User,Pas)
               
        i=i+1