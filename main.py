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
    observatori_fabra = []
    zoo = []
    raval = []
    zona_universitaria = []

    for row in data:
        fecha_lectura = row['DATA_LECTURA']
        estacio = row["CODI_ESTACIO"]
        tipo = row["ACRÒNIM"]
        if tipo == "TM":
            if fecha_lectura:
                fecha = datetime.strptime(fecha_lectura, '%Y-%m-%d')
                if fecha.month == 2:
                    dia_del_mes = int(fecha.strftime('%d'))
                    febrero_data.append(row)
                    febrero_dias.append(dia_del_mes)
                    if estacio == "D5":
                        observatori_fabra.append(float(row['VALOR']))
                    elif estacio == "X2":
                        zoo.append(float(row['VALOR'])) 
                    elif estacio == "X4":
                        raval.append(float(row['VALOR']))
                    elif estacio == "X8":
                        zona_universitaria.append(float(row['VALOR']))
                    else:
                        # Manejo de estaciones desconocidas
                        pass

    max_length = max(len(febrero_dias), len(observatori_fabra), len(zoo), len(raval), len(zona_universitaria))
    febrero_dias += [0] * (max_length - len(febrero_dias))
    observatori_fabra += [0.0] * (max_length - len(observatori_fabra))
    zoo += [0.0] * (max_length - len(zoo))
    raval += [0.0] * (max_length - len(raval))
    zona_universitaria += [0.0] * (max_length - len(zona_universitaria))

    return febrero_dias, observatori_fabra, zoo, raval, zona_universitaria

def visualitza_temperatura_febrer(dias, valors1, valors2, valors3, valors4):
    plt.plot(dias, valors1, label='Observatori Fabra')
    plt.plot(dias, valors2, label='Zoo')
    plt.plot(dias, valors3, label='Raval')
    plt.plot(dias, valors4, label='Zona Universitaria')
    plt.xlabel('Día de Febrero')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura Mitjana a Febrer de 2022')
    plt.legend()
    plt.savefig('grafico_temperatura_febrero.png')



def main():
    meteocat_metadades, meteocat_metadades_2020, meteocat_metadades_2022 = llegir_dades('MeteoCat_Metadades.csv', '2020_MeteoCat_Estacions.csv', '2022_MeteoCat_Detall_Estacions.csv' )
    
    array_metadades = numpy.array(meteocat_metadades)
    array_metadades_2020 = numpy.array(meteocat_metadades_2020)
    array_metadades_2022 = numpy.array(meteocat_metadades_2022)
    
    febrero_dias_2022, observatori_fabra, zoo, raval, zona_universitaria  = filtra_febrero(meteocat_metadades_2022)
    
    visualitza_temperatura_febrer(febrero_dias_2022, observatori_fabra, zoo, raval, zona_universitaria)


main()