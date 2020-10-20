# annual_rate = 4/100
import sys

def get_monthly_rate(annual):
    """
    Calculate monthly rate from annual rate

    price*(1 + annual) = price*(1 + monthly)**12

    >>> get_monthly_rate(.0)  
    0.0
    >>> round(get_monthly_rate(.04), 6)
    0.003274
    >>> round(get_monthly_rate(1.0), 5)
    0.05946
    """

    monthly = (1 + annual)**(1/12) - 1
    # breakpoint()
    return monthly

def get_monthly_payment(amount, annual, months):
    """
    Return payment size required to pay of a load of
    amount (kr) over given number of months at interest rate
    (annual)

    1: amount*(1 + monthly) - payment
    2: amount*(1 + monthly)**2 - payment*(1 + monthly)  - payment
    3: amount*(1 + monthly)**3 - payment*(1 + monthly)**2  - payment*(1 + monthly) - payment
    ...
    after months: 0 = amount*(1 + monthly)**months - sum(k=0, months-1) payment*(1 + monthly)**k

    payment = amount*(1 + monthly)**months/sum(k=0, months-1)(1 + monthly)**k

    where

    sum(k=0, months-1)(1 + monthly)**k = ((1 + monthly)**months - 1)/(monthly)
    """

    monthly = get_monthly_rate(annual)
    denominator = sum((1 + monthly)**k for k in range(months))

    return round(amount * (1 + monthly)**months/denominator)


def main():
    annual_rate = float(sys.argv[1])/100
    monthly_rate = get_monthly_rate(annual_rate)
    print("Monthly rate", round(100*monthly_rate, 2), '%')


if __name__ == "__main__":
    main()