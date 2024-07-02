import pytest
from ops import BankAccount

@pytest.fixture
def acct():
    my_acct = BankAccount(500)
    return my_acct


def test_widthdraw(acct):
    bal = acct.widthdraw(100)
    assert bal == 400 

def test_deposit(acct):
    new_bal = acct.deposit(200)
    assert new_bal == 700
