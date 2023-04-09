import csv
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from django.http import HttpResponse
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

catalog_list = []

def save(ar):
    global catalog_list
    catalog_list.to_csv('catalog_list.csv',index=False)
    return HttpResponse('SUCCESS')

def parse_data(data, class_names, catalog_name, catalog_price):
    for product in data:
        name = product.find_element_by_class_name(class_names["name"]).text
        price = product.find_element_by_class_name(class_names["price"]).text
        catalog_name.append(name)
        catalog_price.append(price)


def parser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(url)

    global catalog_list
    catalog_name, catalog_price = [],[]
        
    data = driver.find_elements_by_class_name('b-catalog-sections_item_holder')
    parse_data(data, {"name":"b-catalog-sections_item_title", "price": "bx_price"}, catalog_name, catalog_price)
    response = requests.get(driver.current_url)
    soup = BeautifulSoup(response.text, "lxml")
    names = soup.find_all('div', class_="b-catalog-sections_item_title")

    catalog_list = pd.DataFrame({'Name': catalog_name, 'Price': catalog_price})
    driver.quit()
