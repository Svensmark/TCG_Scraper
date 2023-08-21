from csvhandler import readNewestDataFromAll
import pandas as pd

dir = "Holdings/PokemonCards/"
df = readNewestDataFromAll(dir)

def getSumOfColoumn(df: pd.DataFrame, coloumnName: str):
    coloumnList = df[coloumnName].to_list()
    coloumnSum = []
    for val in coloumnList:
        coloumnSum.append(float(val))
    sum = 0
    for i in coloumnSum:
        sum += i
    return sum


print(f"Trend: {getSumOfColoumn(df,'Trend')}")
print(f"30-days-trend: {getSumOfColoumn(df,'30-days-trend')}")
print(f"7-days-trend: {getSumOfColoumn(df,'7-days-trend')}")
print(f"1-day-trend: {getSumOfColoumn(df,'1-day-trend')}")