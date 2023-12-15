# healthdatapy.py

import requests
import pandas as pd
import matplotlib.pyplot as plt

class HealthDataPy:
    def __init__(self, base_url="https://www.who.int/data/gho/info/gho-odata-api"):
        """Initialize the HealthDataPy with the API base URL."""
        self.base_url = base_url

    def get_data(self, endpoint, params=None):
        """Fetch data from the specified WHO GHO OData API endpoint."""
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def clean_data(self, data):
        """Clean and preprocess the data fetched from the API."""
        df = pd.DataFrame(data)
        df.dropna(inplace=True)  # Example of cleaning: removing missing values.
        return df

    def aggregate_data(self, data, by):
        """Aggregate data based on specified criteria."""
        return data.groupby(by).mean()  # Example of aggregation: calculating mean.

    def plot_data(self, data, plot_type='line'):
        """Create a plot from the given data."""
        if plot_type not in ['line', 'bar']:
            raise ValueError("Unsupported plot type. Choose 'line' or 'bar'.")
        plot = data.plot(kind=plot_type)
        plt.show()
        return plot

    def api_status_check(self):
        """Check the operational status of the WHO GHO OData API."""
        response = requests.get(self.base_url)
        return response.status_code == 200
