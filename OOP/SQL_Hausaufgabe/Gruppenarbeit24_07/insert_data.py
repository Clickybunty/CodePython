import sqlite3 

def insert_data(): 
# 
    conn = sqlite3.connect('netklix.db') 
    cursor = conn.cursor() 
# 
    genres = [ 
(1, 'Action'), 
(2, 'Komödie'), 
(3, 'Drama'), 
(4, 'Horror'), 
(5, 'Science Fiction') 
] 
    cursor.executemany('INSERT INTO Genre (id, name) VALUES (?, ?)', genres) 
# 
    schauspieler = [ 
(1, 'Tom Hanks', 1956), 
(2, 'Leonardo DiCaprio', 1974), 
(3, 'Scarlett Johansson', 1984), 
(4, 'Robert Downey Jr.', 1965), 
(5, 'Natalie Portman', 1981) 
] 
    cursor.executemany('INSERT INTO Schauspieler (id, name, geburtsjahr) VALUES (?, ?, ?)', schauspieler) 
# 
    rankings = [ 
(1, 'Inception', 5, 2, 8.8), 
(2, 'The Avengers', 1, 4, 8.0), 
(3, 'Forrest Gump', 3, 1, 8.8), 
(4, 'Black Widow', 1, 3, 6.7), 
(5, 'V for Vendetta', 5, 5, 8.2) 
] 
    cursor.executemany('INSERT INTO Ranking (id, titel, genre_id, schauspieler_id, bewertung) VALUES (?, ?, ?, ?, ?)', rankings) 
# 
    conn.commit() 
    conn.close() 
    print("Daten erfolgreich eingefügt.")