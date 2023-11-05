import numpy
import csv
from datetime import datetime
#import matplotlib.pyplot as plt

def llegir_dades(nom_fitxer, nom_fitxer_2, nom_fitxer_3):
    meteocat_metadades = []
    meteocat_metadades_2020 = []
    meteocat_metadades_2022 = []
    with open(nom_fitxer, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            meteocat_metadades.append(row)
    with open(nom_fitxer_2, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            meteocat_metadades_2020.append(row)
    with open(nom_fitxer_3, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            meteocat_metadades_2022.append(row)
    return meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022

def filtra_febrero(data):
    febrero_data = []

    for row in data:
        fecha_lectura = row['DATA_LECTURA']
        if fecha_lectura:
            fecha = datetime.strptime(fecha_lectura, '%Y-%m-%d')
            if fecha.month == 2:
                febrero_data.append(row)
    return febrero_data

def main():
    meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022 = llegir_dades('MeteoCat_Metadades.csv', '2020_MeteoCat_Estacions.csv', '2022_MeteoCat_Detall_Estacions.csv' )
    
    array_metadades = numpy.array(meteocat_metadades)
    array_metadades_2020 = numpy.array(meteocat_metadades_2020)
    array_metadades_2022 = numpy.array(meteocat_metadades_2022)
    #print(meteocat_metadades)
    #print(meteocat_metadades_2020)
    #print(meteocat_metadades_2022)
    
    
    febrero_data_2022 = numpy.array(filtra_febrero(meteocat_metadades_2022))
    for row in febrero_data_2022:
        print(row)
    #xpoints = febrero_data_2022["DATA_LECTURA"]
    #ypoints = febrero_data_2022["VALOR"]
    #plt.plot(xpoints, ypoints)
    #plt.show()

   


main()