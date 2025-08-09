import pytest
from unittest.mock import patch
from src.readers.csv_reader import read_transactions_csv

@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{"amount": 100}]
    result = read_transactions_csv("fake.csv")
    assert result == [{"amount": 100}]
    mock_read_csv.assert_called_once_with("fake.csv")
