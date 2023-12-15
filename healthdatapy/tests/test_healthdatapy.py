# test_healthdatapy.py

import pytest
from unittest.mock import patch, Mock
from healthdatapy import HealthDataPy

@pytest.fixture
def health_api():
    """Fixture to create a HealthDataPy instance for testing."""
    return HealthDataPy()

@patch('healthdatapy.requests.get')
def test_get_data(mock_get, health_api):
    """Test the get_data method with a mocked API call."""
    # Setup mock response
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = {'data': 'test'}

    # Call the method
    result = health_api.get_data('endpoint')

    # Assert the results
    assert result == {'data': 'test'}
    mock_get.assert_called_once()

def test_clean_data(health_api):
    """Test the clean_data method with example data."""
    test_data = {'column1': [1, 2, None, 4], 'column2': [4, None, 6, 8]}
    cleaned_data = health_api.clean_data(test_data)
    assert not cleaned_data.isnull().values.any()

def test_aggregate_data(health_api):
    """Test the aggregate_data method with example data."""
    test_data = pd.DataFrame({
        'category': ['A', 'A', 'B', 'B'],
        'value': [10, 20, 30, 40]
    })
    aggregated_data = health_api.aggregate_data(test_data, ['category'])
    assert aggregated_data.loc['A']['value'] == 15

@patch('healthdatapy.plt.show')
def test_plot_data(mock_show, health_api):
    """Test the plot_data method with example data and a mocked plot display."""
    test_data = pd.DataFrame({'column1': [1, 2, 3, 4]})
    # Test for supported plot types without raising an error
    health_api.plot_data(test_data, 'line')
    health_api.plot_data(test_data, 'bar')
    # Test for an unsupported plot type and expect a ValueError
    with pytest.raises(ValueError):
        health_api.plot_data(test_data, 'pie')

@patch('healthdatapy.requests.get')
def test_api_status_check(mock_get, health_api):
    """Test the api_status_check method with a mocked API call."""
    mock_get.return_value = Mock(status_code=200)
    assert health_api.api_status_check() is True
    mock_get.return_value = Mock(status_code=404)
    assert health_api.api_status_check() is False
