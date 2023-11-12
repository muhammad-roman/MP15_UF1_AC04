import numpy
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import random


def llegir_dades(nom_fitxer_3):
   meteocat_metadades_2022 = []
   with open(nom_fitxer_3, 'r') as file:
       csv_reader = csv.DictReader(file, delimiter=',')
       next(csv_reader)
       for row in csv_reader:
           meteocat_metadades_2022.append(row)
   return meteocat_metadades_2022


def filtra_febrero(data):
   febrero_data = []
   febrero_dias = []
   observatori_fabra = []
   zoo = []
   raval = []
   zona_universitaria = []
   precipitacio = []


   for row in data:
       fecha_lectura = row['DATA_LECTURA']
       estacio = row["CODI_ESTACIO"]
       tipo = row["ACRONIM"]
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
       if tipo == "PPT":
           if fecha_lectura:
               fecha = datetime.strptime(fecha_lectura, '%Y-%m-%d')
               if fecha.month == 2:
                   if float(row["VALOR"]) > 0:
                       precipitacio.append(True)
                   else:
                       precipitacio.append(False)
              


   return febrero_dias, observatori_fabra, zoo, raval, zona_universitaria, precipitacio


def visualitza_temperatura_febrer(dias, valors1, valors2, valors3, valors4):
   dias_feb = numpy.array(list(set(dias)))
   #grafico con todos
   plt.plot(dias_feb, valors1, label='Observatori Fabra', marker= ".")
   plt.plot(dias_feb, valors2, label='Zoo', marker= ".")
   plt.plot(dias_feb, valors3, label='Raval', marker= ".")
   plt.plot(dias_feb, valors4, label='Zona Universitaria', marker= ".")
   plt.xlabel('Día de Febrero')
   plt.ylabel('Temperatura (°C)')
   plt.title('Temperatura Mitjana a Febrer de 2022')
   plt.grid(True)
   plt.legend()
   plt.savefig('grafico_temperatura_febrero.png')


   #grafico subplot
   plt.figure(figsize=(8, 10))


   # 1
   plt.subplot(411)
   plt.plot(dias_feb, valors1, label='Observatori Fabra', marker= ".")
   plt.title('Observatori Fabra')
   plt.xlabel('')
   plt.ylabel('Temperatura (°C)')
   plt.grid(True)
   plt.legend()


   # 2
   plt.subplot(412)
   plt.plot(dias_feb, valors2, label='Zoo', marker= ".", color='yellow')
   plt.title('Zoo')
   plt.xlabel('')
   plt.ylabel('Temperat44.7ura (°C)')
   plt.grid(True)
   plt.legend()


   # 3
   plt.subplot(413)
   plt.plot(dias_feb, valors3, label='Raval', marker= ".", color='green')
   plt.title('Raval')
   plt.xlabel('')
   plt.ylabel('Temperatura (°C)')
   plt.grid(True)
   plt.legend()


   # 4
   plt.subplot(414)
   plt.plot(dias_feb, valors4, label='Zona Universitaria', marker= ".", color='red')
   plt.title('Zona Universitaria')
   plt.xlabel('Día de Febrero')
   plt.ylabel('Temperatura (°C)')
   plt.grid(True)
   plt.legend()


  
   plt.tight_layout()
   plt.suptitle('Temperatura Media en Febrero de 2022', y=0.999)
   plt.savefig('grafico_temperatura_febrero_subplot.png')




def histograma_febrer_2023(fabra, zoo, raval, zona_universitaria):
   temperatura_total = zip(fabra, zoo, raval, zona_universitaria)
   mitjana_total_per_dia = [sum(t) / len(t) for t in temperatura_total]
   array_random = [random.choice(mitjana_total_per_dia) + random.random() for _ in range(len(mitjana_total_per_dia))]
  
   plt.figure()
   plt.hist(array_random, bins=5, edgecolor='black', alpha=0.7, color = "red")
   plt.xlabel('Temperatura media')
   plt.ylabel('Cantidad de dias')
   plt.xlim(-10, 25)
   plt.xticks(range(-10, 26, 2))
   plt.title('Histograma de Temperaturas en Febrero 2023')
   plt.grid(True)
   plt.savefig('histograma_temperatura_febrero_2023.png')


def precipitacio_febrer_2023(precipitacio):
   print(precipitacio)

def prediccion_lluvia_febrero_2023():
    # Suponiendo 28 días en febrero
    dias_febrero_2023 = 28
    
    # Generar predicciones aleatorias de lluvia para cada día
    predicciones = numpy.random.choice([True, False], size=dias_febrero_2023)
    
    return predicciones

def visualizar_prediccion(predicciones):
    # Calcular la proporción de días con y sin lluvia
    dias_con_lluvia = numpy.sum(predicciones)
    dias_sin_lluvia = len(predicciones) - dias_con_lluvia

    # Crear un diagrama de sectores
    plt.figure(figsize=(8, 8))
    plt.pie([dias_con_lluvia, dias_sin_lluvia], labels=['Lluvia', 'Sin lluvia'], autopct='%1.1f%%', startangle=90, colors=['blue', 'lightgrey'])
    plt.title('Proporción de días con y sin lluvia en febrero de 2023')
    plt.savefig('diagrama_sectores_prediccion.png')
    plt.show()

    # Crear un diagrama de barras vertical
    plt.figure(figsize=(8, 4))
    plt.barh(['Lluvia', 'Sin lluvia'], [dias_con_lluvia, dias_sin_lluvia], color=['blue', 'lightgrey'])
    plt.xlabel('Número de días')
    plt.title('Número de días con y sin lluvia en febrero de 2023')
    plt.savefig('diagrama_barras_prediccion.png')
    plt.show()

def precipitacio_febrer_2023(precipitacio):
    visualizar_prediccion(precipitacio)




def main():
    meteocat_metadades_2022 = llegir_dades('2022_MeteoCat_Detall_Estacions.csv' )
    array_metadades_2022 = numpy.array(meteocat_metadades_2022)
  
    febrero_dias_2022, observatori_fabra, zoo, raval, zona_universitaria, precipitacio  = filtra_febrero(array_metadades_2022)
  
    visualitza_temperatura_febrer(febrero_dias_2022, observatori_fabra, zoo, raval, zona_universitaria)
    histograma_febrer_2023(observatori_fabra, zoo, raval, zona_universitaria)
    
    # Obtener la predicción de lluvia para febrero de 2023
    predicciones = prediccion_lluvia_febrero_2023()
    
    precipitacio_febrer_2023(predicciones)

main()
