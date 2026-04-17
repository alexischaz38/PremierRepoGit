import csv
import os

# Spécifiez le chemin de votre fichier CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "testCSV.csv")

# Lire et afficher les données du CSV
with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Afficher l'en-tête
    header = next(csv_reader)
    print(header)
    
    # Afficher les lignes
    for row in csv_reader:
        print(row)