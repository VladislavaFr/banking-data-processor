from src.utils.json_reader import read_json_file
import tempfile
import json


def test_read_valid_json():
    data = [{"description": "test"}]
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    result = read_json_file(tmp_path)
    assert result == data


def test_read_invalid_file():
    result = read_json_file("nonexistent.json")
    assert result == []
