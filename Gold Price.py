import pandas as pd
import requests
import sqlite3
import matplotlib.pyplot as plt

# Downloading the dataset
url = 'https://datahub.io/core/gold-prices/r/monthly.csv'
df = pd.read_csv(url)
print(df.head())

# Data cleaning
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

conn = sqlite3.connect('gold_price.db')
df.to_sql('gold_price', conn, if_exists='replace', index=False)

# Querying the database
plt.plot(df['Date'], df['Price'])
plt.title('Gold Price Trend')
plt.xlabel('Date')
plt.ylabel('Price (USD/oz)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()