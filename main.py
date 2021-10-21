# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

apple_prices = pd.read_csv("apple_prices.csv")
print(apple_prices)
apple_prices_var = apple_prices['open'].var()
print(apple_prices_var)

start = datetime(2008,1,1)
end = datetime(2018,1,1)
gas_prices = web.DataReader('APUS12A74714','fred',start,end)
print(gas_prices)

