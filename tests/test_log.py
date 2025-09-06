import os
import pytest
from src.decorators.log import log


def test_log_to_console_success(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0)" in captured.out


def test_log_to_file_success(tmp_path):
    log_file = tmp_path / "logfile.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(2, 4)
    assert result == 8

    content = log_file.read_text()
    assert "multiply ok" in content


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "errorlog.txt"

    @log(filename=str(log_file))
    def faulty(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty(1, 0)

    content = log_file.read_text()
    assert "faulty error: ZeroDivisionError" in content
    assert "Inputs: (1, 0)" in content
