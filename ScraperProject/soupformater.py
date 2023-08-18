import datetime
import pandas as pd
import bs4
import re

#Returns dataframe of card prices
def getCMPricesPokemonCard(soup: bs4.BeautifulSoup) -> pd.DataFrame:
    # Correct HTML
    print('Formating HTML ..')
    tabContentInfo = soup.find(id="tabContent-info")
    dt = tabContentInfo.findAll("dt", class_="col-6")
    dd = tabContentInfo.findAll("dd", class_="col-6")
    print('HTML formated!')

    #Formating and slicing HTML toString
    contentList = []

    if (len(dd) == 10):
        print('Slicing as unique card with no reprints ..')
        for i in range (4,10):
            sliced_info = str(dd[i])[27:]
            contentList.append(formatSlicedInfo(sliced_info))
    elif (len(dd) == 11):
        print('Slicing as card with reprints ..')
        for i in range (5,11):
            print(dd[i])
            sliced_info = str(dd[i])[27:]
            contentList.append(formatSlicedInfo(sliced_info))
    print('Successfully sliced! '+ str(contentList))

    #Create Dataframe with data from above    
    print('Creating dataframe of slice ..')
    df = createDataFrame(contentList)
    print('Dataframe created!')
    return df


# Returns string of name
def getName(soup: bs4.BeautifulSoup) -> str:
    print('Retrieving card name ..')
    h1_tag_string = str(soup.find_all("h1").pop())
    string_builder = ""
    count = 0
    for char in h1_tag_string:
        if (count >= 4):
            if (char != '<'):
                string_builder += char
            else:
                print('Retrieved card name!: ' + string_builder)
                return string_builder
        count += 1


def formatSlicedInfo(si: str) -> str:
    si = si.replace("</dd>","")
    si = si.replace("<span>","")
    si = si.replace("</span>","")
    si = si.replace(" €","")
    si = si.replace(",",".")
    return si


def createDataFrame(contentList: list[str]) -> pd.DataFrame:
    print('Creating data ..')

    from_price = float(re.findall(r'[\d,.]+', contentList[1])[0])
    trend_price = float(re.findall(r'[\d,.]+', contentList[2])[0])
    thirty_days_avg = float(re.findall(r'[\d,.]+', contentList[3])[0])
    seven_days_avg = float(re.findall(r'[\d,.]+', contentList[4])[0])
    one_day_avg = float(re.findall(r'[\d,.]+', contentList[5])[0])

    d = {'Date': datetime.date.today(), 'Amount available': int(contentList[0]), 'From price': from_price, 'Trend price': trend_price, '30-days average price': thirty_days_avg, '7-days average price': seven_days_avg, '1-day average price': one_day_avg}
    print('Data created!: '+str(d))
    print('Creating dataframe object ..')
    df = pd.DataFrame(data=d, index=[0])
    print('Dataframe object created!:\n'+str(df))
    return df