# ValuePy: A library for value investing using Python
# ValuePy is a Python library that provides tools for value investing. It can be used to load, analyze and visualize financial data of stocks. It also allows you to set projections for future financial performance of the stock and calculates various financial metrics.

from valuepy import Stock

# Create a Stock object
```
stock = Stock("AAPL", start_year=2010)
```
# Load financial data
Use standardized format as prescribed in format.xlsx , import kpi's etc here. the load_data() method is based on this format.
```
stock.load_data("AAPL_financials.xlsx")
```
# Set projections for future financial performance
```
projections = {"growth": 0.05, "earnings": 10}
stock.set_projections(projections)
```
# Calculate various financial metrics and your own custom metrics 
```
stock.calculate_metrics()
```
# Plot the progress of a KPI compared to projected values
```
stock.plot_kpi("price")
```
# Generate summary of all the metrics
```
stock.summary()
```

#You can also add your custom metrics by passing the metric name and calculation function, for example:

```
def current_ratio(data):
    """Calculate the current ratio of a stock"""
    return data["current_assets"] / data["current_liabilities"]
    
stock.add_metric("Current Ratio", current_ratio)
```

# Load and save stock objects containing projections and data: 

```
stock.save_pickle(filepath)
ticker = function.load_pickle(filepath)
```


Please let me know if you need any other information to be added in the readme.
