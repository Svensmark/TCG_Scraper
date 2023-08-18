
def readHoldings(txt: str) -> list[str]:
    print('Reading Holdings.txt ..')
    with open(txt) as f:
        lines = f.readlines()
        f.close()
        print('Reading successful!')
        return lines
        
