import matplotlib.pyplot as plt
from datetime import datetime

def analyze_sport_data(data):
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in
    data['Datum']]
    teams = list(set(data['Team']))
    plt.figure(figsize=(10, 6))
    for team in teams:
        team_dates = [daten[i] for i in range(len(daten)) if data['Team'][i]
        == team]
        team_scores = [data['Tore'][i] for i in range(len(daten)) if
    data['Team'][i] == team]
    plt.plot(team_dates, team_scores, marker='o', label=team)
    plt.title('Leistung der Teams über die Saison hinweg')
    plt.xlabel('Datum')
    plt.ylabel('Tore pro Spiel')
    plt.legend()
    plt.tight_layout()
    plt.show() 