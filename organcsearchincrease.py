import os
import psutil
import time
import datetime
now = datetime.datetime.now()
print("\n")
print("*************************Welcome to Iyantras Vedic Booster Project**************************")
print("\n")
import os
import time
import selenium
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
print("\n")
h=1
i=1
j=1
driver = webdriver.Firefox()
driver.get('https://www.google.com/')
inputElement = driver.find_element_by_id('lst-ib')
inputElement.send_keys('ganapathi homam')
time.sleep(2)
driver.find_element_by_class_name('sbico-c').click()
time.sleep(4)
driver.switch_to.window(driver.window_handles[-1])
def ganapathy():
    print("ganapathy")
    driver.get("http://www.vedicfolks.com/art-sports/karma-remedies/homams/maha-ganapathi-homam-.html")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
    time.sleep(3)
    inputElement = driver.find_element_by_id('txt_firstname')
    inputElement.send_keys('lalitavishaka')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element_by_link_text("Shared homam").click()
    time.sleep(8)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[2]/a").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
    time.sleep(3)   
    for process in (process for process in psutil.process_iter() if process.name()=="firefox.exe"):
        process.kill()
while True:
    while j<10:
        print("1")
        try:
            if (j==2):
                '''
                try:
                    driver = webdriver.Firefox()
                    driver.get('https://www.google.com/')
                    inputElement = driver.find_element_by_id('lst-ib')
                    inputElement.send_keys('ganapathi homam')
                    time.sleep(2)
                    driver.find_element_by_class_name('sbico-c').click()
                    time.sleep(4)
                    driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
                    a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
                    time.sleep(2)
                    ganapathy()
                 except NoSuchElementException:
                     h=1
                     print("except")
                     print("5",h)
                     h=h+1;
                     driver.find_element_by_link_text(str(h)).click()
                     time.sleep(3)
                  '''  
                #driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
                #a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
                #time.sleep(2)
                ##if(a>1):
                    ##print("fun")driver = webdriver.Firefox()
                driver.get('https://www.google.com/')
                inputElement = driver.find_element_by_id('lst-ib')
                inputElement.send_keys('ganapathi homam')
                time.sleep(2)
                driver.find_element_by_class_name('sbico-c').click()
                time.sleep(4)
                #driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
                #a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
                #time.sleep(2)
                ##if(a>1):
                    ##print("fun")

                    
                print("3",j)
                driver = webdriver.Firefox()
                driver.get('https://www.google.com/')
                inputElement = driver.find_element_by_id('lst-ib')
                inputElement.send_keys('ganapathi homam')
                time.sleep(2)
                driver.find_element_by_class_name('sbico-c').click()
                time.sleep(4)
                #driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
                #a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
                #time.sleep(2)
                ##if(a>1):
                    ##print("fun")
                    ##break
                '''
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
                a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
                time.sleep(2)
                if(a>1):
                    print("sup")
                print("Website found in ",i,"page")
                time.sleep(4)
                j=j+1
                ganapathy()
                '''
            print("4")
            #driver.switch_to.window(driver.window_handles[-1])
            driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()
            a=len(str(driver.find_element_by_link_text("Maha Ganapathi Homam - Vedicfolks").click()))
            time.sleep(2)
            if(a>1):
                print("sup")
            print("Website found in ",i,"page")
            j=j+1
            time.sleep(4)
            ganapathy()
        except NoSuchElementException:
            i=1
            print("except")
            print("5",i)
            i=i+1;
            driver.find_element_by_link_text(str(i)).click()
            time.sleep(3)
            
