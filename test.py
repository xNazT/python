import pytest
from account import *

class Test:
    def setup_method(self):
        self.testaccount = Account("test")

    def tear_down_method(self):
        del self.testaccount


    def test_init(self):
        assert self.testaccount.get_name() == "test"
        assert self.testaccount.get_balance() == pytest.approx(0)


    def test_deposit(self):
        assert self.testaccount.deposit(-5) is False
        assert self.testaccount.get_balance() == pytest.approx(0)
        assert self.testaccount.deposit(0) is False
        assert self.testaccount.get_balance() == pytest.approx(0)
        assert self.testaccount.deposit(50) is True
        assert self.testaccount.get_balance() == pytest.approx(50)


    def test_withdraw(self):
        assert self.testaccount.withdraw(-5) is False
        assert self.testaccount.get_balance() == pytest.approx(0)
        assert self.testaccount.withdraw(0) is False
        assert self.testaccount.get_balance() == pytest.approx(0)
        assert self.testaccount.withdraw(50) is False
        assert self.testaccount.get_balance() == pytest.approx(0)
        self.testaccount.deposit(100)
        assert self.testaccount.withdraw(50) is True
        assert self.testaccount.get_balance() == pytest.approx(50)
