#Automation using Selenium

from selenium import webdriver
import time

# we need to check about the version of chrome and then serach "Google Chromedriver" in Google Chrome. Then download the chromedriver according system's chrome version and check which device we are using.
driver = webdriver.Chrome('C:\Users\Rupayan\OneDrive\Documents\Automation using Python\venv\chromedriver.exe')  #change the path file
driver.maximize_window()
time.sleep(3)
driver.get('https://in.search.yahoo.com/search;_ylt=AwrPrCPc6rdjRg0OLnzmHAx.?p=beauty+of+kolkata&type=E211IN714G0&fr=mcafee&fr2=p%3As%2Cv%3Av%2Cm%3Apivot&stype=web')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/div/div/div/div/ol/li[5]/div/div/ul/li[1]/div/a/div[2]/p[2]').click()  #here we've copied the xpath path, we can also copy the html or css path
time.sleep(5) 
driver.find_element_by_name('search_query').send_keys('Beauty Of West Bengal')
time.sleep(3)
driver.find_element_by_xpath('#again copy the xpath').click() 
driver.refresh()
driver.title()
driver.close()
