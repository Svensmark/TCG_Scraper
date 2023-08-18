import bs4
import pandas as pd
import re
import datetime


def handleSoups(soups_list: list[bs4.BeautifulSoup]):
    """ Returns List of dicts with structure { product name: dataframe of prices } based on a list of BS4 soups """
    dict_list = []
    
    for soup in soups_list:
    # TODO: Find type af SOUP
    # soupType = getSoupType(soup):
    # if (soupType == PokemonCard)
        cardName = pc_getCardPrice(soup)
        dataframe = pc_getCardName(soup)
        
        dict_list.append({cardName: dataframe})
    # elif (soupType == SealedMagicProduct)
        # etc..

    return dict_list



def pc_getCardName(soup: bs4.BeautifulSoup) -> str:
    """Returns string of name based on a single BS4 soup (of a Pokemon Card)"""
    h1_tag_string = str(soup.find_all("h1").pop())
    string_builder = ""
    count = 0
    for char in h1_tag_string:
        if (count >= 4):
            if (char != '<'):
                string_builder += char
            else:
                return string_builder
        count += 1



# pc - PokemonCard
def pc_getCardPrice(soup: bs4.BeautifulSoup) -> pd.DataFrame:
    """Returns pandas.DataFrame of prices based on a single BS4 soup (of a Pokemon Card)"""
    tab_content_info = soup.find(id="tabContent-info")
    dd = tab_content_info.findAll("dd", class_="col-6")

    sliced_info_list = []

    # Different types of cards
    # Sliced info = [<div>trend price</div>, <div>amount available</div>] etc. (not exact values)
    if (len(dd) == 10):
        for i in range (4,10):
            sliced_info = str(dd[i])[27:]
            sliced_info_list.append(formatSlicedInfo(sliced_info))
    elif (len(dd) == 11):
        for i in range (5,11):
            sliced_info = str(dd[i])[27:]
            sliced_info_list.append(formatSlicedInfo(sliced_info))

    #Create Dataframe with data from above    
    df = createDataFrame(sliced_info_list)
    return df



def formatSlicedInfo(sliced_info: str) -> str:
    """ Removes HTML leaving only values - Example Input: "<dd>value</dd>" ->  Output: "value" """
    sliced_info = sliced_info.replace("</dd>","")
    sliced_info = sliced_info.replace("<span>","")
    sliced_info = sliced_info.replace("</span>","")
    sliced_info = sliced_info.replace(" €","")
    sliced_info = sliced_info.replace(",",".")
    return sliced_info



def createDataFrame(sliced_info_list: list[str]) -> pd.DataFrame:
    """ Creates a dataframe of a list of the sliced info of a single card - List containing all prices of a card"""
    amount_available = int(sliced_info_list[0])
    from_price = float(re.findall(r'[\d,.]+', sliced_info_list[1])[0])
    trend_price = float(re.findall(r'[\d,.]+', sliced_info_list[2])[0])
    thirty_days_avg = float(re.findall(r'[\d,.]+', sliced_info_list[3])[0])
    seven_days_avg = float(re.findall(r'[\d,.]+', sliced_info_list[4])[0])
    one_day_avg = float(re.findall(r'[\d,.]+', sliced_info_list[5])[0])

    d = {'Date': datetime.date.today(), 'Amount available': amount_available, 'From price': from_price, 'Trend price': trend_price, '30-days average price': thirty_days_avg, '7-days average price': seven_days_avg, '1-day average price': one_day_avg}

    df = pd.DataFrame(data=d, index=[0])
    
    return df