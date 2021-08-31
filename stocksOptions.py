# Stock Stalker Pro Options


class Trade():
    def __init__(self, ticker, openPrice, closePrice, optionType='NA'):
        self.__list = [ticker, openPrice, closePrice, optionType]
        self.__open = openPrice
        self.__close = closePrice
        self.__ticker = ticker.upper()
        self.__type = optionType.upper()
        self.__profit = closePrice - openPrice
        self.__percentChange = self.__profit / self.__open * 100

    def getOpen(self):
        return self.__open
    def getClose(self):
        return self.__close
    def getTicker(self):
        return self.__ticker
    def getType(self):
        return self.__type
    def getList(self):
        return self.__list

    def __str__(self):
        return self.__ticker  +" Option: "+self.__type+'\n'+\
               "  Open: ${:.2f}".format(self.__open)+'\n'+\
               "  Close: ${:.2f}".format(self.__close)+'\n'+\
               "  Profit: ${:.2f}".format(self.__profit)+'\n'+\
               "  Percent chg:{:.2f}%".format(self.__percentChange)+'\n'

class tickerTrades():
    '''All the trade objects for a ticker'''
    
    def __init__(self, ticker):
        self.__ticker = ticker
        self.__tradeList = []
        self.__percentTotal = 0
        self.__profitTotal = 0

    def addTrade(self, trade):
        self.__tradeList.append(trade)
        
    def getTradeList(self):
        return self.__tradeList
    def getPercentTotal(self):
        return self.__percentTotal
    def getProfitTotal(self):
        return self.__profitTotal
    
    def setTotals(self):
        openTotal = 0
        closeTotal = 0
        percentTotal = 0
        profitTotal = 0
        for i in self.__tradeList:
            openTotal += i.getOpen()
            closeTotal += i.getClose()
            
        self.__profitTotal = closeTotal - openTotal
        self.__percentTotal = self.__profitTotal / openTotal * 100


    def printTrades(self):
        print("All "+self.__ticker+" Trades")
        for i in self.__tradeList:
            if i: print(i)
        print()
    def __str__(self):
        return "TICKER: "+self.__ticker+"\nTOTALS:\n  Percent chg: {:.2f}%"\
               .format(self.__percentTotal)+"\n"+"  Profit: ${:.2f}"\
               .format(self.__profitTotal)+'\n'



class AllTrades():
    '''Stores tickerTrade lists in a dictionary with
    ticker as key, list as val'''
    def __init__(self):
        self.__tradeDict = {}

    def getTradeDict(self):
        return self.__tradeDict
    def addTrade(self, trade):
        if trade.getTicker() not in self.__tradeDict.keys():
            self.__tradeDict[trade.getTicker()] = \
                tickerTrades(trade.getTicker())
        self.__tradeDict[trade.getTicker()].addTrade(trade)
        self.__tradeDict[trade.getTicker()].setTotals()


def enterTrades(allTrades, fileName):
    print("Enter your trades manually, leave ticker blank to quit")

    while True:
        ticker = input("Ticker: ")
        if not ticker: break
        option = input("Contract Type: ")
        openP = eval(input("Open Price: "))
        closeP = eval(input("Close Price "))
        print('-----\n')

        trade = Trade(ticker, openP, closeP, option)
        allTrades.addTrade(trade)
    print("\nDone entering trades\n")
    writeFile(allTrades, fileName)
    print("Wrote to file: {}".format(fileName))
        

def printBriefStats(port):
    print("All Tickers Brief Stats\n")
    for i in port.getTradeDict(): print(port.getTradeDict()[i])
    print('-----\n')

def printAllTrades(port):
    print("All Trades by Ticker\n")
    print('-----\n')
    for i in port.getTradeDict(): print(port.getTradeDict()[i].printTrades())


def lineBreak():
    print('-----\n')

###################################
##### Read and Write Files


def openFile(fileName):
    import csv
 
    tradeList = []
    port = AllTrades()
    with open(fileName, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            if row:
                trade = Trade(row[0],eval(row[1]),eval(row[2]),row[3])
                tradeList.append(trade)
                line_count += 1
        line_count -= 1
        print(f'Processed {line_count} trades.')

    for i in tradeList:
        port.addTrade(i)
    return port


def writeFile(port, filename):
    import csv
    # field names 
    fields = ['ticker','open','close','type'] 
        
    # data rows of csv file 
    rows = []
    for i in port.getTradeDict().values():
        for j in i.getTradeList():
            rows.append(j.getList())
        
        
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
    
    
def main():
    fileName = 'trades.txt'
    port = openFile(fileName)
    
    while True:
        print()
        print("STOCK STALKER OPTIONS PRO")
        print()
        print("1: Enter Trade\n2. Brief Stats\n3. All Trades Details\n"+\
              "q: Quit\n")
        entry = input("Enter the number of the action above: ")
        print()
        if entry == '1': enterTrades(port, fileName)
        elif entry == '2':  printBriefStats(port)
        elif entry == '3': printAllTrades(port)
        elif entry.upper() == 'Q': break
        else:
            print("Bad Entry, enter 1, 2, or 3")
            continue
        print()
        stop = input('q to quit, return to continue: ')
        if stop.upper() == 'Q':
            break
        
    print("\nQuitting")
                                                                   
main()       
    
# test stuff
'''
a = Trade('QQQ',150,200,'C')
b = Trade('QQQ', 100,200,'P')
c = Trade('TTT',120,100)

D = AllTrades()
D.addTrade(a)
D.addTrade(b)
D.addTrade(c)
'''
#fileName = 'trades.txt'
#port = openFile(fileName)
#D = enterTrades(port, fileName)
'''
print("All Tickers Brief Stats\n")
for i in D.getTradeDict(): print(D.getTradeDict()[i])
print('-----\n')
print("All Trades by Ticker\n")
print('-----\n')
for i in D.getTradeDict(): print(D.getTradeDict()[i].printTrades())
'''
                                                               
'''
L = tickerTrades('QQQ')
L.addTrade(a)
L.addTrade(b)
L.addTrade(c)
L.setTotals()

print(D)
print('------')
'''

