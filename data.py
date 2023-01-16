import yfinance as yf
import pandas as pd

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = {}
    data['earnings'] = stock.earnings
    data['balance_sheet'] = stock.balance_sheet
    data['cashflow'] = stock.cashflow
    data['major_holders'] = stock.major_holders
    data['calendar'] = stock.calendar
    data['dividends'] = stock.dividends
    data['splits'] = stock.splits
    return data


def retrieve_data_row(stock_data,col_name,row_name):
    return pd.DataFrame(stock_data[col_name]).T[row_name]



# data = get_stock_data('LEE')
# print(data['splits'])