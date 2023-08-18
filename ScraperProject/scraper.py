from bs4 import BeautifulSoup
from selenium import webdriver
import time

def getSoup(url_list: list[str]):
    print('Retrieving soupsList ..')
    #Selenium
    driver = webdriver.Chrome()
    soupsList = []

    #Retrieves soup for each URL site in given list
    count = 1
    for url in url_list:
        driver.get(url)
        #Getting correct HTML
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        soupsList.append(soup)
        print(f'Finished scraping site {count} / {len(url_list)} ..')
        count += 1
        time.sleep(1)

    print('Soups retrieved!')
    return soupsList