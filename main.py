import pandas as pd
import pickle
import matplotlib.pyplot as plt


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = None
        self.projections = {}

    def load_data(self, filepath):
        """Load data from a standardized Excel file"""
        self.data = pd.read_excel(filepath)

    def set_projections(self, projections):
        """Set projected financial KPI's for the stock"""
        self.projections = projections

    def save_pickle(self, filepath):
        """Save the Stock object to a pickle file"""
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_pickle(filepath):
        """Load a Stock object from a pickle file"""
        with open(filepath, 'rb') as f:
            return pickle.load(f)

    def plot_kpi(self, kpi):
        """Plot the progress of a specific KPI compared to projections"""
        kpi_data = self.data[kpi]
        projection = self.projections[kpi]
        plt.plot(kpi_data, label='Actual')
        plt.plot(projection, label='Projected')
        plt.xlabel('Period')
        plt.ylabel(kpi)
        plt.legend()
        plt.show()