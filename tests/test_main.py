import pytest
from app import main


class TestBase:
    def test_hello_dss(self):
        message = main.hello_dss()
        assert message == "Dear Developer, welcome in this sample repository!"

    @pytest.mark.describe("Check wrong value")
    def test_hello_dss_exceptions(self):
        with pytest.raises(ValueError):
            message = main.hello_dss(666)
