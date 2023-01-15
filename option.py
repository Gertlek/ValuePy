import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class option:
    def __init__(self, is_put, is_short, strike_price, price, expiry_date):
        self.is_put = is_put
        self.is_short = is_short
        self.strike_price = strike_price
        self.price = price
        self.expiry_date = expiry_date
        self.time_to_maturity = self.calculate_time_to_maturity()

    def calculate_time_to_maturity(self):
        """Calculates time to maturity in years"""
        today = datetime.datetime.now().date()
        time_to_maturity = (self.expiry_date - today).days / 365
        return time_to_maturity



    def return_long(self, stock_price):
        """Calculates the  return of going short"""
        if self.is_put:
            cash_flow = [-self.price, max(self.strike_price - stock_price, 0)]
        else:
            cash_flow = [-self.price, max(stock_price - self.strike_price, 0)]

        return (cash_flow[1] / abs(cash_flow[0]))  - 1


    def return_short(self, stock_price):
        """Calculates the  return of going short"""
        if self.is_put:
            cash_flow = [self.price, min(stock_price - self.strike_price, 0)]

        else:

            cash_flow = [self.price, min(self.strike_price - stock_price, 0)]

        return cash_flow[1]  + self.price




    def return_range(self, stock_price_range, price_step, plot=False):
        """Calculates the IRR of going short/long for different levels around the price"""
        stock_prices = np.arange(stock_price_range[0], stock_price_range[1], price_step)
        returns = []
        for stock_price in stock_prices:
            if self.is_short:
                returns.append(self.return_short(stock_price))
            else:
                returns.append(self.return_long(stock_price))

        if plot == True:
            df = pd.DataFrame([stock_prices, returns]).T
            df.columns = ["Stock Price", "Option CF"]
            df.plot()
            plt.grid()

            plt.show()

        cagr = (np.array(returns)/self.strike_price) * 100 / (self.time_to_maturity ) # with strike?
        cagr = np.round(cagr, 2)
        df = pd.DataFrame([stock_prices, returns, cagr]).T
        df.columns = ['Stock price', 'Return', 'CAGR']
        return df


# expiry_date = datetime.date(2023, 6,1)
#
# call = option(True, True, 17, 1.5, expiry_date)
#
# # print(pd.DataFrame(call.return_short_range([5,15],1/2,plot = True)))
# # plt.show()
#
# print(call.return_range([10,23],1/2,plot = True))
# plt.show()