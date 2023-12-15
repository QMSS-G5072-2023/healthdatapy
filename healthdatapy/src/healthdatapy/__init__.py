# read version from installed package
from importlib.metadata import version
__version__ = version("healthdatapy")

# healthdatapy/__init__.py
from healthdatapy.api import get_data
from healthdatapy.data_processing import clean_data, aggregate_data
from healthdatapy.visualization import plot_data
from healthdatapy.utils import api_status_check
