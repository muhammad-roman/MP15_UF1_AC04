import numpy
import csv

def llegir_dades(nom_fitxer, nom_fitxer_2, nom_fitxer_3):
    meteocat_metadades = []
    meteocat_metadades_2020 = []
    meteocat_metadades_2022 = []
    with open(nom_fitxer, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            meteocat_metadades.append(row)
    with open(nom_fitxer_2, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            meteocat_metadades_2020.append(row)
    with open(nom_fitxer_3, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            meteocat_metadades_2022.append(row)
    return meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022

def main():
    meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022 = llegir_dades('MeteoCat_Metadades.csv', '2020_MeteoCat_Estacions.csv', '2022_MeteoCat_Detall_Estacions.csv' )
    
    array_metadades = numpy.array(meteocat_metadades)
    array_metadades_2020 = numpy.array(meteocat_metadades_2020)
    array_metadades_2022 = numpy.array(meteocat_metadades_2022)
    #print(meteocat_metadades)
    #print(meteocat_metadades_2020)
    #print(meteocat_metadades_2022)


main()