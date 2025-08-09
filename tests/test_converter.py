
from src.external_api.converter import convert_to_rubles
from unittest.mock import patch


@patch("src.external_api.converter.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90}}

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"}
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 900.0


def test_convert_rub_to_rub():
    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 1000.0
