from decimal import Decimal
from forex_python.bitcoin import BtcConverter
from datetime import datetime
from rich import print

# Check Bitcoin prices
b = BtcConverter()
print(f'1 BTC = {b.get_latest_price("USD")} USD')


# Currency conversion
from forex_python.converter import CurrencyRates

c = CurrencyRates()

# get popular conversion rates for USD
# print(c.get_rates('USD'))

# get conversion rate for specific currency
print(c.get_rate("USD", "EUR"))

# get conversion rate for specific currency at some date
date_obj = datetime(2020, 10, 20, 12, 10, 10, 151012)
print(c.get_rate("USD", "INR", date_obj=date_obj))

# convert from xxx to xxx + amount
print(c.convert("USD", "INR", 1))

# convert from xxx to xxx + amount at some date
print(c.convert("USD", "EUR", 1, date_obj=date_obj))

# Detect use of Decimal
print(c.convert("USD", "INR", Decimal("10.45")))
print(c.convert("USD", "INR", 10))
