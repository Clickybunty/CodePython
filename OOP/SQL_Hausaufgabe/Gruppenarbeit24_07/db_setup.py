import sqlite3 
# 
def create_tables(): 
    conn = sqlite3.connect('netklix.db') 
    cursor = conn.cursor() 
# 
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Genre ( 
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL 
) 
''') 
# 
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Schauspieler ( 
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL, 
geburtsjahr INTEGER NOT NULL 
) 
''') 
# 
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Ranking ( 
id INTEGER PRIMARY KEY, 
titel TEXT NOT NULL, 
genre_id INTEGER NOT NULL, 
schauspieler_id INTEGER NOT NULL, 
bewertung REAL NOT NULL, 
FOREIGN KEY (genre_id) REFERENCES Genre(id), 
FOREIGN KEY (schauspieler_id) REFERENCES Schauspieler(id) ) 
''') 
# 
    conn.commit() 
    conn.close() 
    print("Tabellen erfolgreich erstellt.")