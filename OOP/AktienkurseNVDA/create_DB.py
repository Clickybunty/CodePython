import sqlite3

def create_database():
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS stock_data
              (date TEXT PRIMARY KEY, close REAL)
              ''')
    conn.commit()
    conn.close()