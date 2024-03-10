#Tarea 3 (Simulacion de estado financiero de una empresa)
import itertools
import random
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.stats import norm

n = 100

a = list(itertools.repeat(0, n))                #Lista de generacion de numeros aleatorios para activo operativo neto
proyeccionActivo = list(itertools.repeat(0, n)) #Lista donde se guardan las simulaciones de activo operativo neto
zA = list(itertools.repeat(0, n))               #Z de los activo operativo neto

#p = list(itertools.repeat(0, n))                #Lista de generacion de numeros aleatorios para pasivo financiero
proyeccionPasivo = list(itertools.repeat(0, n)) #Lista donde se guardan las simulaciones de pasivo financiero

v = list(itertools.repeat(0, n))                #Lista de generacion de numeros aleatorios para ventas
proyeccionVentas = list(itertools.repeat(0, n)) #Lista donde se guardan las simulaciones de ventas

g = list(itertools.repeat(0, n))                #Lista de generacion de numeros aleatorios para ganancias operativas
proyeccionGanacias = list(itertools.repeat(0, n)) #Lista donde se guardan las simulaciones de ganancias operativas
zG = list(itertools.repeat(0, n))               #Z de las ganancias operativas

c = list(itertools.repeat(0, n))                #Lista de generacion de numeros aleatorios para costo pasivo financiero
proyeccionCosto = list(itertools.repeat(0, n)) #Lista donde se guardan las simulaciones de costo pasivo financiero

for i in range(0, n, 1):
    a[i] = random.uniform(0, 1)
    zA[i] = norm.ppf(a[i])
    proyeccionActivo[i] = 170 * zA[i] + 1000

    proyeccionPasivo[i] = random.uniform(260, 290)

    v[i] = random.uniform(0, 1)
    proyeccionVentas[i] = -(1100 * math.log(v[i]))
    
    g[i] = random.uniform(0, 1)
    zG[i] = norm.ppf(g[i])
    proyeccionGanacias[i] = 20 * zG[i] + 130

    c[i] = random.uniform(0, 1)
    proyeccionCosto[i] = -(22 * math.log(v[i]))

#Imprimir la media de las proyecciones
print("Resumen de las medias de las proyecciones")
promedioA = sum(proyeccionActivo) / len(proyeccionActivo)
print("\nPromedio de activo operativo neto:", promedioA)

promedioP = sum(proyeccionPasivo) / len(proyeccionPasivo)
print("\nPromedio de pasivo financiero:", promedioP)

promedioV = sum(proyeccionVentas) / len(proyeccionVentas)
print("\nPromedio de ventas:", promedioV)

promedioG = sum(proyeccionGanacias) / len(proyeccionGanacias)
print("\nPromedio de ganancias operativas:", promedioG)

promedioC = sum(proyeccionCosto) / len(proyeccionCosto)
print("\nPromedio de costo pasivo financiero:", promedioC)

# Crear un DataFrame de pandas
data2 = {'Aletorio1':a, 'zA':zA, 'Activo':proyeccionActivo, 'Pasivo': proyeccionPasivo, 'Aleatorio3': v, 
         'Ventas':proyeccionVentas,'Aleatorio4':g,'zG':zG,'Ganancias':proyeccionGanacias, 'Aleatorio5':c, 'Costo':proyeccionCosto}
df2 = pd.DataFrame(data2)

# Exportar el DataFrame a un archivo Excel
df2.to_excel('datos3.xlsx', index=False)