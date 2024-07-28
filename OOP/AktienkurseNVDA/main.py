from create_DB import create_database
from fetchAndSave import fetch_stock_data, save_to_database
from plot import plot_stock_data
from analyze import analyze_stock_data

def main():
    
    create_database()    
    data = fetch_stock_data()    
    save_to_database(data)    
    plot_stock_data()    
    analyze_stock_data()
    avg_change = analyze_stock_data()
    
    print(f'Die durchschnittliche Preisänderung pro Tag beträgt: {avg_change:.2f}')
    
if __name__ == "__main__":
    main()
