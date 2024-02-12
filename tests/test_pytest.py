import pytest
from divide import dividePy
from main import add, multiply

def test_dividePy():
    assert dividePy(10, 2) == 5
    assert dividePy(-10, 2) == -5
    assert dividePy(10, -2) == -5
    assert dividePy(-10, -2) == 5
    assert dividePy(10, 0) is None

def test_add():
    assert add(3,7) == 10

def test_multiply(mocker):
    mocker.patch('main.add', return_value=15, autospec=True)
    result = multiply(3, 5)
    assert result == 15