
import csv

#Extract
def llegir_dades(nom_fitxer):
    dades = []
    with open(nom_fitxer, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            dades.append(row)
    return dades



def main():
    dades = llegir_dades('/home/sjo/Escriptori/DADES/RomanAziz/python_exercices/MP15-UF1-AC04/MeteoCat_Metadades.csv')
    print_dades(dades)
    print(dades)

    