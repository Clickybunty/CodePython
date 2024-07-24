from db_setup import create_database
from insert_data import insert_weather_data, fetch_weather_data
from matplot_data import analyze_weather_data

def main():
# Schritt 1: Datenbank erstellen
    create_database()
# Schritt 2: Beispieldaten einfügen
    insert_weather_data()
# Schritt 3: Daten abrufen und analysieren
    data = fetch_weather_data()
    analyze_weather_data(data)

if __name__ == "__main__":
    main()