import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt

start = datetime.datetime(2019,1,1)
end = datetime.datetime(2020,1,1)
s = "LBTYA"
df = pdr.DataReader(s,'yahoo',start,end)
df["Close 20 days mean"] = df["Close"].rolling(20).mean()
df["Upper"] = df["Close"].rolling(20).mean() + (df["Close"].rolling(20).std()) * 2
df["Lower"] = df["Close"].rolling(20).mean() - (df["Close"].rolling(20).std()) * 2
ax = df[["Close","Close 20 days mean","Upper","Lower"]].tail(100).plot(figsize=(16,6))
ax.yaxis.grid(True)
ax.xaxis.grid(True)
plt.show()