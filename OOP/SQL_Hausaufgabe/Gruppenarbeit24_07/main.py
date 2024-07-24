from db_setup import create_tables 
from insert_data import insert_data 
# 

def main(): 
    create_tables() 
    insert_data() 
    
# __name__ == "__main__": 
# Dies ist der Fall, 
# wenn das Skript direkt ausgeführt wird. 
# Das bedeutet, 
# dass das Skript nicht importiert wird, 
# sondern direkt von der Kommandozeile oder 
# einer IDE gestartet wird.
if __name__ == "__main__": 
    main()
