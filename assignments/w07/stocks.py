# stocks.py
#
# usage:   match entry to dictionary of stocks
# input:   ticker symbol
# output:  ticker symbol and price
# 
# Dictionary of stock prices
stocks = {'aaa':111, 'bbb':222, 'ccc': 333, 'ddd': 444, 'eee': 555, 'fff': 666, 'ggg': 777, 'hhh': 888, 'iii': 999, 'jjj': 0}

while(True):
    
    ticker = input('Enter stock ticker (or type exit to close): ').lower()

    # exit loop if user inputs exit request
    if ticker == 'exit':
        break
    # use get to auto-produce error?
    elif ticker in stocks.keys():
        print('\nStock ticker: ' + ticker.upper() + '\nValue: ' + str('{:}'.format(stocks[ticker])))
    else:
        print("Please check entry for typo: ",ticker)

