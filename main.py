import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np


class Stock:
    def __init__(self, stock_name, start_year=None):
        if start_year is None:
            raise ValueError("You must provide a start year")
        self.name = stock_name
        self.start_year = start_year
        self.data = None
        self.projections = None
        self.metrics = None

    def load_data(self, filepath):
        """Load data from a standardized Excel file"""
        self.data = pd.read_excel(filepath)

    def set_projections(self, projections): # needs to be genral
        """Set projected financial KPI's for the stock"""
        self.projections = projections

    def save_pickle(self, filepath):
        """Save the Stock object to a pickle file"""
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    def plot_kpi(self, kpi):
        """Plots progress of a KPI compared to projected values"""
        kpi_data = self.data[self.data.year >= self.start_year]
        plt.plot(kpi_data.year, kpi_data[kpi], label="Actual")
        if self.projections:
            plt.plot(self.projections.index, self.projections[kpi], label="Projected")
        plt.xlabel("Year")
        plt.ylabel(kpi)
        plt.legend()
        plt.show()

    def calculate_metrics(self):
        """Calculate various financial metrics"""
        self.metrics = {}
        self.metrics["P/E"] = self.data["price"] / self.data["earnings"]
        self.metrics["ROE"] = self.data["net_income"] / self.data["equity"]
        self.metrics["ROA"] = self.data["net_income"] / self.data["assets"]
        self.metrics["Dividend Yield"] = self.data["dividend"] / self.data["price"]
        self.metrics["Debt-to-equity"] = self.data["debt"] / self.data["equity"]

    def calculate_metrics(self):
        """Calculate various financial metrics"""
        self.metrics = {}
        required_columns = [["price", "earnings"], ["net_income", "equity"], ["net_income", "assets"], ["dividend", "price"], ["debt", "equity"]]
        for columns in required_columns:
            if all(col in self.data.columns for col in columns):
                if columns == ["price", "earnings"]:
                    self.metrics["P/E"] = self.data["price"] / self.data["earnings"]
                elif columns == ["net_income", "equity"]:
                    self.metrics["ROE"] = self.data["net_income"] / self.data["equity"]
                elif columns == ["net_income", "assets"]:
                    self.metrics["ROA"] = self.data["net_income"] / self.data["assets"]
                elif columns == ["dividend", "price"]:
                    self.metrics["Dividend Yield"] = self.data["dividend"] / self.data["price"]
                elif columns == ["debt", "equity"]:
                    self.metrics["Debt-to-equity"] = self.data["debt"] / self.data["equity"]
            else:
                if columns == ["price", "earnings"]:
                    self.metrics["P/E"] = float('nan')
                elif columns == ["net_income", "equity"]:
                    self.metrics["ROE"] = float('nan')
                elif columns == ["net_income", "assets"]:
                    self.metrics["ROA"] = float('nan')
                elif columns == ["dividend", "price"]:
                    self.metrics["Dividend Yield"] = float('nan')
                elif columns == ["debt", "equity"]:
                    self.metrics["Debt-to-equity"] = float('nan')

    def add_metric(self, metric_name, calculation_function):
        """Add a custom metric to the Stock object"""
        self.metrics[metric_name] = calculation_function(self.data)


    def summary(self):
        """Returns all the metrics neatly"""
        self.calculate_metrics()
        for key, value in self.metrics.items():
            print(key, ":", value)

    def dcf(self, discount_rate, buyback_rate):
        """Calculate the discounted cash flow value of the stock using the projected financial KPI's"""
        if self.projections is None:
            raise ValueError("You must set projections before calculating DCF")
        dcf_value = 0
        for i in range(len(self.projections)):
            dcf_value += (self.projections.iloc[i]["free_cash_flow"] * (1 + buyback_rate)**i) / (1 + discount_rate)**i
        return dcf_value

#projections = pd.DataFrame({"year": [2021, 2022, 2023], "free_cash_flow": [100, 120, 140]})

