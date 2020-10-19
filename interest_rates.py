# annual_rate = 4/100
import sys

def get_monthly_rate(annual):
    """
    Calculate monthly rate from annual rate

    price*(1 + annual) = price*(1 + monthly)**12
    """
    monthly = (1 + annual)**(1/12) - 1
    return monthly


if __name__ == "__main__":
    annual_rate = float(sys.argv[1])/100
    monthly_rate = get_monthly_rate(annual_rate)
    print("Monthly rate", round(100*monthly_rate, 2), '%')