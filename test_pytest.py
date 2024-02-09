from divide.divide import dividePy
import pytest

class TestPytest:
    
    def test_pytest_dividePy(self):
        assert dividePy(10, 2) == 5
        assert dividePy(-10, 2) == -5
        assert dividePy(10, -2) == -5
        assert dividePy(-10, -2) == 5
        with pytest.raises(ZeroDivisionError):
            dividePy(10, 0)