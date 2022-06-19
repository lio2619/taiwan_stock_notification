from requests.exceptions import Timeout
from bs4 import BeautifulSoup as bs

import requests
import csv
import os

def read_csv_dict(stock_name):
    stock_name_and_code = {}

    with open('../stock_code.csv', 'r') as file:
        read = csv.reader(file)

        for i in read:
            stock_name_and_code[i[1]] = i[0]

    try:
        return stock_name_and_code[stock_name]
    except:
        return stock_name

def stock_price(stock_code):
    headers = {'user-agent' : 'Mozilla/5.0'}

    try:
        res = requests.get("https://www.google.com/finance/quote/%s:TPE" %stock_code, headers = headers, timeout = 10)      #如果網站響應時間超過10秒，就跳出去
        html = res.text
        res.close()                                     #把requests關掉
    except Timeout:
        print("website takes too long to respond")
        os._exit()
    except:
        print("your stock name is wrong")
        os._exit()

    soup = bs(html, 'lxml')
    
    try:
        receive_stock_price = soup.find('div', class_ = 'YMlKec fxKbKc').text
    except:
        print("div class name is wrong")
        os._exit()

    return receive_stock_price

if __name__ == '__main__':
    stock_name = input("please enter stock name\n")
    stock_code = read_csv_dict(stock_name)
    stock_price(stock_code)