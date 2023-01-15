ValuePy: A library for value investing using Python
ValuePy is a Python library that provides tools for value investing. It can be used to load, analyze and visualize financial data of stocks. It also allows you to set projections for future financial performance of the stock and calculates various financial metrics.

Getting started
To install ValuePy, you can use pip:

Copy code
pip install valuepy
Usage
Here's an example of how to use the ValuePy library to load data for a stock, set projections, calculate metrics and plot the progress of a KPI:

Copy code
from valuepy import Stock

# Create a Stock object
stock = Stock("AAPL", start_year=2010)

# Load financial data
stock.load_data("AAPL_financials.xlsx")

# Set projections for future financial performance
projections = {"growth": 0.05, "earnings": 10}
stock.set_projections(projections)

# Calculate various financial metrics
stock.calculate_metrics()

# Plot the progress of a KPI compared to projected values
stock.plot_kpi("price")

# Generate summary of all the metrics
stock.summary()
You can also add your custom metrics by passing the metric name and calculation function, for example:

Copy code
def current_ratio(data):
    """Calculate the current ratio of a stock"""
    return data["current_assets"] / data["current_liabilities"]
    
stock.add_metric("Current Ratio", current_ratio)
You can also visualize the data with the help of different plotting libraries like matplotlib, seaborn etc.

Note
Please note that the above example is just an illustration, the actual projections and their keys will depend on the specific use case and data available.

Contributing
If you're interested in contributing to ValuePy, please take a look at our contributing guidelines for more information.

Support
If you have any questions or issues with ValuePy, please open an issue on the issue tracker or contact the maintainers directly.

License
ValuePy is released under the MIT License.

Please let me know if you need any other information to be added in the readme.
