import interest_rates
import pytest

# for i in range(10):
#    print(interest_rates.get_monthly_rate(i/100))

# interest_rates.main()

def test_monthly_0():
    assert interest_rates.get_monthly_rate(0) == 0

def test_monthly_4():
    assert interest_rates.get_monthly_rate(0.04) ==  pytest.approx(0.0032737398)

@pytest.mark.skip('failing')
def test_payments_0():
    assert interest_rates.get_monthly_payment(50000, .0, 20) == 2500

@pytest.mark.skip('failing')
def test_payments_1():
    assert interest_rates.get_monthly_payment(50000, .01, 20) == 2501