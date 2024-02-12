from divide import dividePy

class TestPytest:
    
    def test_pytest_dividePy(self):
        assert dividePy(10, 2) == 5
        assert dividePy(-10, 2) == -5
        assert dividePy(10, -2) == -5
        assert dividePy(-10, -2) == 5
        assert dividePy(10, 0) is None