import soupformater as sf
import portfolioreader as pf
import scraper
import csvhandler as ch
import time

# Holdings is a .txt file that contains links of every item holding
holdingstxt = "Holdings/Holdings.txt"
holdingsUrlList = pf.readHoldings(holdingstxt)

# Retrives list of soups
soupsList = scraper.getSoup(holdingsUrlList)

# Retrieves dataframe of todays pricing of each url
count = 1
for soup in soupsList:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    # Scrapes the card name
    cardName = sf.getName(soup)
    # Scrapes the trend price etc.
    df = sf.getCMPricesPokemonCard(soup)
    # append data frame to CSV file
    ch.writeToCSV(cardName, df)
    print(f'Finished writing to csv for {count} / {len(soupsList)} ..')
    count += 1

#Der skal tages højde for hidden div ('number') Jammer kort
#Der skal tages højde for andre valuta Mewtwo kort
#Begge er nederste i holdings.txt
#Lave under mappe til pokemon kort holdings Holdings/PokemonCards/xx
#Skrive todos ind i notions