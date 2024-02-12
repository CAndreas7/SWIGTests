import pytest
from divide import dividePy
from main import add, multiply
from unittest.mock import patch

def test_dividePy():
    assert dividePy(10, 2) == 5
    assert dividePy(-10, 2) == -5
    assert dividePy(10, -2) == -5
    assert dividePy(-10, -2) == 5
    assert dividePy(10, 0) is None
    assert dividePy(0, 10) == 0
    assert dividePy(0, -10) == 0
    assert dividePy(0, 0) is None

def test_add():
    assert add(3,7) == 10
    assert add(-3,7) == 4
    assert add(3,-7) == -4
    assert add(-3,-7) == -10

def test_multiply():
    with patch('main.add', return_value=15) as mock_add:
        result = multiply(3, 5)
        assert result == 15
        assert mock_add.call_count == 5

    with patch('main.add', return_value=0) as mock_add:
        result = multiply(0, 5)
        assert result == 0
        assert mock_add.call_count == 5
        
    with patch('main.add', return_value=-15) as mock_add:
        result = multiply(-3, 5)
        assert result == -15
        assert mock_add.call_count == 5
    
    with patch('main.add', return_value= -6) as mock_add:
        result = multiply(2, -3)
        assert result == -6
        assert mock_add.call_count == 3