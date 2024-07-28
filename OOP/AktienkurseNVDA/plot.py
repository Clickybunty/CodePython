import matplotlib.pyplot as plt
import sqlite3

def plot_stock_data():
    
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    c.execute('''
              SELECT date, close FROM stock_data ORDER BY date
              ''')
    rows = c.fetchall()
    conn.close()

    dates = [row[0] for row in rows]
    closes = [row[1] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, closes, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Prices over the Last Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

