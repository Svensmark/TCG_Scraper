from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas
from scraper.souphandler import handleSoups

def getPriceDataframe(url_list: list[str]) -> list[pandas.DataFrame]:
    """ Returns a list of DataFrames cointaing prices of each card in URL list. """
    soups_list = scrapeSoups(url_list)
    return handleSoups(soups_list)

def scrapeSoups(url_list: list[str]) -> list[BeautifulSoup]:
    """ Retrieves a list of URLS and returns a list of BS4 soups for each URL. """
    #Selenium
    driver = webdriver.Chrome()
    soups_list = []

    # Retrieves soup for each URL site in given list
    for url in url_list:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        soups_list.append(soup)
        # Sleep to not get request timedout
        time.sleep(1)

    return soups_list