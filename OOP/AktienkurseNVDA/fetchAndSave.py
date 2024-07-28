import requests
import sqlite3

API_KEY = 'DEIN_ALPHA_VANTAGE_API_KEY'
STOCK_SYMBOL = 'NVDA'
BASE_URL = 'https://www.alphavantage.co/query'

def fetch_stock_data():
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_SYMBOL,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data['Time Series (Daily)']
    return time_series

def save_to_database(data):
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    for date, daily_data in data.items():
        close_price = float(daily_data['4. close'])
        c.execute('''
                  INSERT OR REPLACE INTO stock_data (date, close)
                  VALUES (?, ?)
                  ''', (date, close_price))
    conn.commit()
    conn.close()
