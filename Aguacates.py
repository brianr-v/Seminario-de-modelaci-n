# Tarea 2 (Simulacion de la produccion de aguacates)
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

def GastosF(u):
    cont = 0
    p = [0.1352, 0.26, 0.4108, 0.55, 0.6904, 0.82, 0.9136, 1 ]
    g = [48, 39, 43, 35, 40, 30, 35, 23]
    
    for j in range(0,n,1):
        if u <= p[j]:
            return g[j]
        cont += 1


def Simulacion_Gastos(n, u1, simGasto):
    #Ciclo para la simulación de gatos
    for i in range(0,n,1):
        u1[i] = random.uniform(0, 1)
        simGasto[i] = GastosF(u1[i])

    promedioG = sum(simGasto) / len(simGasto)
    #print("Simulacion de la produccion de aguacates")
    #print("\nPromedio de gastos:", promedioG)
    # Crear un DataFrame de pandas
    data2 = {'Aletorio1':u1, 'Gastos':simGasto}
    df2 = pd.DataFrame(data2)
    # Exportar el DataFrame a un archivo Excel
    df2.to_excel('datos1.xlsx', index=False)
    return promedioG

def Simulacion_Produccion(n, u2, z, simProdu):
    #Ciclo para la simulación de producción
    for j in range(0,n,1):
        u2[j] = random.uniform(0, 1)
        z[j] = norm.ppf(u2[j])
        simProdu[j] = 160 * z[j] + 1000

    promedioP = sum(simProdu) / len(simProdu)
    #print("\nPromedio de produccion:", promedioP)
    # Crear un DataFrame de pandas
    data2 = {'Aleatorio2':u2, 'z': z, 'Produccion': simProdu}
    df2 = pd.DataFrame(data2)

    # Exportar el DataFrame a un archivo Excel
    df2.to_excel('datos2.xlsx', index=False)
    return promedioP

def Simulacion_Venta(n, u3, simVenta):
    #Ciclo para la simulación de precio de venta
    for l in range(0,n,1):
        u3[l] = random.uniform(0, 1)
        simVenta[l] = (200 - 100)*u3[l] + 100

    promedioV = sum(simVenta) / len(simVenta)
    # Crear un DataFrame de pandas
    data2 = {'Aleatorio3':u3,'Precio':simVenta}
    df2 = pd.DataFrame(data2)

    # Exportar el DataFrame a un archivo Excel
    df2.to_excel('datos3.xlsx', index=False)
    return promedioV
    #print("\nPromedio de precio de venta:", promedioV)

def Ganacias(promedioP, promedioV, promedioG):
    # Ganancias
    #print("\nResultado de la simulacion:")
    ventas = promedioP * promedioV * 1000   # Multiplicamos por 1000 porque son toneladas
    ganacias = ventas - promedioG*1000000

    #print("\nVentas previstas: ", ventas)
    #print("Gastos previstos: ", promedioG*1000000)
    print("Las ganacias previstas son: ", ganacias," de pesos")

    # Crear un DataFrame de pandas
    #data2 = {'Aletorio1':u1, 'Gastos':simGasto, 'Aleatorio2':u2, 'z': z, 'Produccion': simProdu, 'Aleatorio3':u3,'Precio':simVenta,}
    #df2 = pd.DataFrame(data2)

    # Exportar el DataFrame a un archivo Excel
    #df2.to_excel('datos2.xlsx', index=False)

def Precios_Año(promedioV, condicion):
    #Esta funcion genera los precios de venta para el siguiente año como 2024 y 2025
    if condicion == True:
        x = np.random.uniform(0, 0.046) # x = 0.046*u 
        u = np.random.uniform(0, 1)
        x = 1 + (x * u)
    else:
        x = np.random.uniform(0, 0.0315) # x = 0.046*u 
        u = np.random.uniform(0, 1)
        x = 1 + (x * u)

    return promedioV * x


# DATOS DE INICIO
n = 100                                 #Numero de datos a generar
u1 = list(itertools.repeat(0, n))       #Numeros aleatorios para gastos
u2 = list(itertools.repeat(0, n))       #Numeros aleatorios para producción
u3 = list(itertools.repeat(0, n))       #Numeros aleatorios para ventas
simGasto = list(itertools.repeat(0, n)) #Simulacion de los gastos
simProdu = list(itertools.repeat(0, n)) #Simulacion de la produccion
simVenta = list(itertools.repeat(0, n)) #Simulacion de la venta
z = list(itertools.repeat(0, n))
condicion = True                        #Condicion para determinar en que año estamos si es True estamos en 2024

for i in range(1,3):
    if condicion == True:
        print("Simulacion de la produccion de aguacates año 2024")
    else:
        print("\nSimulacion de la produccion de aguacates año 2025")

    # Llamamos a la función de simulacion de GASTOS
    promedioG = Simulacion_Gastos(n, u1, simGasto)
    print("Promedio de gastos:", promedioG)

    # Llamamos a la función de simulacion de PRODUCCION
    promedioP = Simulacion_Produccion(n, u2, z, simProdu)
    print("Promedio de produccion:", promedioP)

    # Llamamos a la función de simulacion de PRECIOS DE VENTA
    promedioV = Simulacion_Venta(n, u3, simVenta)
    #print("Promedio de precio de venta:", promedioV)

    if condicion == True:
        # Llamamos a la funcion de generador de precios del año futuro 2024 o 2025
        promedioV = Precios_Año(promedioV, condicion)
        print("El precio de los aguacates para el 2024 es: ", promedioV)
    else:
        promedioV = Precios_Año(promedioV, condicion)
        print("El precio de los aguacates para el 2025 es: ", promedioV)
    #print("Promedio de precio de venta:", promedioV)

    # Llamamos a la funcion de ganancias
    Ganacias(promedioP, promedioV, promedioG)

    
    condicion = False
