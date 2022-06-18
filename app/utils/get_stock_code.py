from requests.exceptions import Timeout

import requests
import os
import re
import csv

#可以試看看從這邊抓及時股價     https://www.google.com/finance/quote/3481:TPE

def correspondence_table():     #抓取股票代碼對應股票名稱
    table = []
    headers = {'user-agent' : 'Mozilla/5.0'}
    
    try:
        res = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2", headers = headers, timeout = 10)      #如果網站響應時間超過10秒，就跳出去
        html = res.text
        res.close()                                     #把requests關掉
    except Timeout:
        print("website takes too long to respond")
        os.exit()

    oring_table = re.findall('\w*\u3000\w*', html)        #獲得股票代碼的對應表，還沒處理過
    
    for i in oring_table:                   #把股票代碼與名稱分開
        table.append(i.split("\u3000"))     #table[0][0] = 股票代碼(str)     table[0][1] = 股票名稱(str)      table[0] = list

    return table

def data_input_database(table):
    with open('../stock_code.csv', 'w', newline = '') as file:
        write = csv.writer(file)

        for i in table:
            write.writerow(i)

if __name__ == '__main__':
    table = correspondence_table()
    data_input_database(table)