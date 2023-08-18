import scraper.scraper as scraper
import portfolioreader as pf
import csvhandler as ch

# Holdings is a .txt file that contains links of every item holding
holdings_txt_path = "Holdings/Holdings.txt"
holdings_url_list = pf.readHoldings(holdings_txt_path)

# Retrives dataframe based on scrapings of the list of urls
dict_list = scraper.getPriceDataframe(holdings_url_list)

ch.writeDictListToCSV(dict_list)