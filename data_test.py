import pandas as pd
# print ("pandas is ready!")
# data = {
#     "Date": ["Monday", "Tuesday", "Wednesday"],
#     "Open": [100, 110, 105],
#     "Close": [110, 105, 120]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.shape)
# print(df.info())
# print(df.describe())

import yfinance as yf 

stock = yf.Ticker("RELIANCE.NS")
data = stock.history(period="5y", timeout=30,raise_errors=True)
print("Rows and Columns:", data.shape)
print(data.empty)
print(data.head())
print(data.index)
print(data.index[0])
print(type(data))
print(type(data["Close"]))



