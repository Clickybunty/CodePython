import sqlite3

def analyze_stock_data():
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    c.execute('SELECT close FROM stock_data ORDER BY date')
    rows = c.fetchall()
    conn.close()

    prices = [row[0] for row in rows]
    price_changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    avg_price_change = sum(price_changes) / len(price_changes)

    return avg_price_change
