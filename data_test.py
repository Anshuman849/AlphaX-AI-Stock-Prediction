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
print(data.isnull().sum())
print(data.duplicated().sum())
print(data.index.duplicated().sum())
print(data.describe())
# outlier calculation close column

Q1 = data["Close"].quantile(0.25)

Q3 = data["Close"].quantile(0.75)

IQR = Q3 - Q1

highest = Q3 + 1.5*IQR
lower = Q1 - 1.5*IQR
print("highest" , highest)
print("lower" , lower)


outliers = data[
     (data["Close"]< lower)|
     (data["Close"]> highest)
 ]

print("Total outliers:", len(outliers))
print(outliers[["Close"]])

# outlier calculation open column

QO1 = data["Open"].quantile(0.25)
QO3 = data["Open"].quantile(0.75)

IQR2 = QO3 - QO1
Higher  = QO3 + 1.5*IQR2
lowest = QO1 - 1.5*IQR2

print("Higher" , Higher)
print("lowest" , lowest)

Outliers2 = data[
    (data["Open"] < lowest)|
    (data["Open"] > Higher)
]

print("Total outliers2:", len(Outliers2))
print(Outliers2[["Open"]])


# outlier calculation High column

QH1  = data["High"].quantile(0.25)
QH3 = data["High"].quantile(0.75)

IQRH = QH3 - QH1

Lowest = QH1 - 1.5*IQRH
Highest = QH3 + 1.5*IQRH

print("Highest" , Highest)
print("Lowest" , Lowest)

Outliers3 = data[
    (data["High"] < Lowest)|
    (data["High"] > Highest)
]

print("Total outliers3:", len(Outliers3))
print(Outliers3[["High"]])

# outlier calculation Low column

QL1  = data["Low"].quantile(0.25)
QL3 = data["Low"].quantile(0.75)

IQRL = QL3 - QL1

Lowest1 = QL1 - 1.5*IQRL
Highest1 = QH3 + 1.5*IQRL

print("Highest1" , Highest1)
print("Lowest1" , Lowest1)

Outliers4 = data[
    (data["High"] < Lowest1)|
    (data["High"] > Highest1)
]

print("Total outliers4:", len(Outliers4))
print(Outliers4[["Low"]])

# outlier calculation Low column

QL1  = data["Low"].quantile(0.25)
QL3 = data["Low"].quantile(0.75)

IQRL = QL3 - QL1

Lowest1 = QL1 - 1.5*IQRL
Highest1 = QH3 + 1.5*IQRL

print("Highest1" , Highest1)
print("Lowest1" , Lowest1)

Outliers4 = data[
    (data["High"] < Lowest1)|
    (data["High"] > Highest1)
]

print("Total outliers4:", len(Outliers4))
print(Outliers4[["Low"]])

# outlier calculation Low column

QL1  = data["Low"].quantile(0.25)
QL3 = data["Low"].quantile(0.75)

IQRL = QL3 - QL1

Lowest1 = QL1 - 1.5*IQRL
Highest1 = QH3 + 1.5*IQRL

print("Highest1" , Highest1)
print("Lowest1" , Lowest1)

Outliers4 = data[
    (data["High"] < Lowest1)|
    (data["High"] > Highest1)
]

print("Total outliers4:", len(Outliers4))
print(Outliers4[["Low"]])

# outlier calculation Low column

QV1  = data["Volume"].quantile(0.25)
QV3 = data["Volume"].quantile(0.75)

IQRV = QV3 - QV1

Lowest2 = QV1 - 1.5*IQRV
Highest2 = QV3 + 1.5*IQRV

print("Highest2" , Highest2)
print("Lowest2" , Lowest2)

Outliers5 = data[
    (data["Volume"] < Lowest2)|
    (data["Volume"] > Highest2)
]

print("Total outliers5:", len(Outliers5))
print(Outliers5[["Volume"]])

print("Highest Volume :" , data["Volume"].max())
print("Average volume :" , data["Volume"].mean())
print("Median volume :" , data["Volume"].median())
print("Outlier Percentage:", (len(Outliers5)/len(data))*100)

# Data visualisation closing data

import matplotlib.pyplot as plt 

plt.figure(figsize=(12,5))

plt.plot(data.index, data["Close"])
plt.title("Reliance Stock Closing Price (5 Years)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()

# Data visualisation volume data

plt.figure(figsize =(12,5))

plt.plot(data.index , data["Volume"])
plt.title("Reliance Trading Volume (5 Years)")
plt.xlabel("Date")
plt.ylabel("Volume")

plt.show()

# percentage change in closing price 

data["Daily_return"] = data["Close"].pct_change()*100

print(data[["Close" , "Daily_return"]].head(10))

# plotting daily return and volume 

plt.figure(figsize=(10,5))

plt.scatter(data["Volume"],data["Daily_return"])
plt.title("Daily Return vs Trading Volume")
plt.xlabel("Trading Volume")
plt.ylabel("Daily Return (%)")

plt.show()

print(data.loc[data["Volume"].idxmax(), ["Volume", "Daily_return"]])
print(data.loc[data["Volume"].idxmin(), ["Volume", "Daily_return"]])
print(data.loc["2025-03-18"])
print(data.loc["2025-03-17":"2025-03-19"])


