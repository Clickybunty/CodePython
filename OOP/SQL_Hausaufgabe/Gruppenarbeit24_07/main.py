from db_setup import create_tables 
from insert_data import insert_data 
# 

def main(): 
    create_tables() 
    insert_data() 
# 
if __name__ == "__main__": 
    main()
