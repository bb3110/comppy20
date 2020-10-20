import pytest
from leap_year import is_leap_year

@pytest.mark.parametrize(
     'year, expected',
     [
        (2000, True),
        (1999, False),
        (1998, False),
        (1996, True),
        (1900, False),
        (1800, False),
        (1600, True),
     ]
)
def test_leap_year(year, expected):
    assert is_leap_year(year) == expected