import pytest
from operations import add, multiply, divide, subtract
from unittest.mock import patch

def test_dividePy():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
    assert divide(10, 0) is None
    assert divide(0, 10) == 0
    assert divide(0, -10) == 0
    assert divide(0, 0) is None

def test_add():
    assert add(3,7) == 10
    assert add(-3,7) == 4
    assert add(3,-7) == -4
    assert add(-3,-7) == -10

def test_subtract(): 
    assert subtract(1,1) == 0
    assert subtract(2,1) == 1
    assert subtract(1,2) == -1
    assert subtract(-1,-1) == 0
    assert subtract(-1, 1) == -2

def test_multiply():
    with patch('operations.add', return_value=15) as mock_add:
        result = multiply(3, 5)
        assert result == 15
        assert mock_add.call_count == 5

    with patch('operations.add', return_value=0) as mock_add:
        result = multiply(0, 5)
        assert result == 0
        assert mock_add.call_count == 5
        
    with patch('operations.add', return_value=-15) as mock_add:
        result = multiply(-3, 5)
        assert result == -15
        assert mock_add.call_count == 5
    
    with patch('operations.add', return_value= -6) as mock_add:
        result = multiply(2, -3)
        assert result == -6
        assert mock_add.call_count == 3