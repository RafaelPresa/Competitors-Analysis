# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 00:16:47 2022

@author: rafae

source: https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-using-selenium-in-python/
"""

import xlsxwriter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome("/Users/rafae/Downloads/chromedriver_win32/chromedriver")
  
element_list_github = []
dlt_github = ['iotaledger','cosmos','bitcoin','ethereum','ripple','cardano-foundation','elrondnetwork','solana-labs','eos','iotexproject','near','oceanprotocol','vechain']
  
for page_github in enumerate(dlt_github):
    page_url_github = "https://github.com/" + str(page_github[1])
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url_github)
    
    time.sleep(3)   # Delays for X seconds. You can also use a float value.
    
    names_github = driver.find_element_by_class_name('h2.lh-condensed').text
    repositories = driver.find_element_by_class_name('Counter.js-profile-repository-count').text
    people = driver.find_element_by_class_name('Counter.js-profile-member-count').text
  
    element_list_github.append([names_github,repositories,people])
  
element_list_reddit = []
dlt_reddit = ('iota','cosmosnetwork','bitcoin','ethereum','ripple','cardano','dot',
              'elrondnetwork','avax','solana','chainlink','dashpay','eos','hedera',
              'iotex','monero','nearprotocol','oceanprotocol','tezos',
              'vechain')
  
for page_reddit in enumerate(dlt_reddit):
    
    page_url_reddit = "https://www.reddit.com/r/" + str(page_reddit[1])
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url_reddit)
    
    time.sleep(5)   # Delays for X seconds. You can also use a float value.
    
    names_reddit = driver.find_element_by_class_name('_2yYPPW47QxD4lFQTKpfpLQ').text
    members = driver.find_element_by_class_name('_3XFx6CfPlg-4Usgxm0gK8R').text
  
    element_list_reddit.append([names_reddit, members])


with xlsxwriter.Workbook('Competitors_Mult_XLS.xlsx') as workbook:
    
    worksheet1 = workbook.add_worksheet('GitHub')    
    for row_num, data in enumerate(element_list_github):
        worksheet1.write_row(row_num, 0, data)
    
    worksheet2 = workbook.add_worksheet('Reddit')
    for row_num, data in enumerate(element_list_reddit):
        worksheet2.write_row(row_num, 0, data)
    
  
driver.close()






