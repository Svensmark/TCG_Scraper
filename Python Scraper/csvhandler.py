import pandas as pd
import os.path
import datetime
import pathvalidate as v
import os

def writeDictListToCSV(dict_list: list[dict]):
    for dict in dict_list:
        try:
            key = ""
            value = ""
            for i in dict:
                key = i
                value = dict[i]
            writeToCSV(key, value)
        except:
            continue

def writeToCSV(card_name: str, df: pd.DataFrame):
    print('Writing file to csv ..')
    filename = "Holdings/PokemonCards/"+card_name+'.csv'


    if (os.path.isfile(filename)):
        print('Writing to existing file ..')
        with open(filename) as f:
            date_of_newest_row = f.readlines()[-1].split(',')[0]
            if (str(datetime.date.today()) != str(date_of_newest_row)):
                df.to_csv(filename, mode='a', index=False, header=False)
            f.close()
    else: 
        print('Creating new file ..')

        df.to_csv("Holdings/PokemonCards/"+v.sanitize_filename(card_name)+'.csv', mode='a', index=False)


def readNewestDataFromAll(dir_path: str):
    lastRows = []
    for filename in os.listdir(dir_path):
        with open(f"{dir_path}{filename}", "r", encoding="utf-8", errors="ignore") as reader:
            lastRows.append(reader.readlines()[-1].strip().split(','))
    df = pd.DataFrame(lastRows)
    df.columns = ['Date','Amount available','From','Trend','30-days-trend','7-days-trend','1-day-trend']
    return df