# Stock Stalker Pro Options

class Trade():
    def __init__(self, ticker, openPrice, closePrice, optionType='NA'):
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
        for i in self.__tradeList: print(i)
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


def enterTrades():
    allTrades = AllTrades()
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
    return allTrades
        
        
        
                                                               
        
    
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
D = enterTrades()
print("All Tickers Brief Stats\n")
for i in D.getTradeDict(): print(D.getTradeDict()[i])
print('-----\n')
print("All Trades by Ticker\n")
print('-----\n')
for i in D.getTradeDict(): print(D.getTradeDict()[i].printTrades())

                                                               
'''
L = tickerTrades('QQQ')
L.addTrade(a)
L.addTrade(b)
L.addTrade(c)
L.setTotals()

print(D)
print('------')
'''

