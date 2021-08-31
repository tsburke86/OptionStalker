from stocksOptions import *
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
        print(f'Processed {line_count} lines.')

    for i in tradeList:
        port.addTrade(i)
    return port


def writeFile(filename):
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


