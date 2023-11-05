import numpy
import csv
from datetime import datetime
import matplotlib.pyplot as plt

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
    febrero_dias = []
    febrero_valors = []

    for row in data:
        fecha_lectura = row['DATA_LECTURA']
        if fecha_lectura:
            fecha = datetime.strptime(fecha_lectura, '%Y-%m-%d')
            if fecha.month == 2:
                febrero_data.append(row)
                dia_del_mes = int(fecha.strftime('%d'))
                febrero_dias.append(dia_del_mes)
                febrero_valors.append(float(row['VALOR']))
    
    return febrero_data, febrero_dias, febrero_valors

def main():
    meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022 = llegir_dades('MeteoCat_Metadades.csv', '2020_MeteoCat_Estacions.csv', '2022_MeteoCat_Detall_Estacions.csv' )
    
    array_metadades = numpy.array(meteocat_metadades)
    array_metadades_2020 = numpy.array(meteocat_metadades_2020)
    array_metadades_2022 = numpy.array(meteocat_metadades_2022)
    
    #PRINT PRUEBAS
    #print(meteocat_metadades)
    #print(meteocat_metadades_2020)
    #print(meteocat_metadades_2022)
    
    #FEBRERO_DATA_2022 ES FEBRERO FILTRADO, FEBRERO DIAS SON LOS DIAS DE LA COLUMNA "DATA_LECTURA", FEBRERO VALORES SON LA COLUMNA VALOR DEL CSV (DE 2022_MATEOCAT_DETALL_ESTACIONS.CSV)
    febrero_data_2022, febrero_dias_2022, febrero_valors_2022 = filtra_febrero(meteocat_metadades_2022)
    
    
    #PRUEBAS (FUNCIONA, PERO HAY QUE HACER LA GRAFICA DE LOS DIAS (HECHO) Y TEMPERATURA (SIN HACER))

    #print(febrero_valors_2022)
    #xpoints = numpy.array(febrero_dias_2022)
    #ypoints = numpy.array(febrero_valors_2022)
    #plt.plot(xpoints, ypoints)
    #plt.show()

   


main()