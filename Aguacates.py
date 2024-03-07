# Tarea 2 (Simulacion de la produccion de aguacates)
import itertools
import random
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


#Datos de inicio
n = 100                                 #Numero de datos a generar
u1 = list(itertools.repeat(0, n))       #Numeros aleatorios para gastos
u2 = list(itertools.repeat(0, n))       #Numeros aleatorios para producción
u3 = list(itertools.repeat(0, n))       #Numeros aleatorios para ventas
simGasto = list(itertools.repeat(0, n)) #Simulacion de los gastos
simProdu = list(itertools.repeat(0, n)) #Simulacion de la produccion
simVenta = list(itertools.repeat(0, n)) #Simulacion de la venta
z = list(itertools.repeat(0, n))

#Ciclo para la simulación de gatos
for i in range(0,n,1):
    u1[i] = random.uniform(0, 1)
    simGasto[i] = GastosF(u1[i])

promedioG = sum(simGasto) / len(simGasto)
print("Simulacion de la produccion de aguacates")
print("\nPromedio de gastos:", promedioG)


#Ciclo para la simulación de producción
for j in range(0,n,1):
    u2[j] = random.uniform(0, 1)
    z[j] = norm.ppf(u2[j])
    simProdu[j] = 160 * z[j] + 1000

promedioP = sum(simProdu) / len(simProdu)
print("\nPromedio de produccion:", promedioP)

#Ciclo para la simulación de precio de venta
for l in range(0,n,1):
    u3[l] = random.uniform(0, 1)
    simVenta[l] = (200 - 100)*u3[l] + 100

promedioV = sum(simVenta) / len(simVenta)
print("\nPromedio de precio de venta:", promedioV)

# Ganancias
print("\nResultado de la simulacion:")
ventas = promedioP * promedioV * 1000   # Multiplicamos por 1000 porque son toneladas
ganacias = ventas - promedioG*1000000

print("\nVentas previstas: ", ventas)
print("Gatos previstos: ", promedioG*1000000)
print("Las ganacias previstas son: ", ganacias)

# Crear un DataFrame de pandas
data2 = {'Aletorio1':u1, 'Gastos':simGasto, 'Aleatorio2':u2, 'z': z, 'Produccion': simProdu, 'Aleatorio3':u3,'Precio':simVenta,}
df2 = pd.DataFrame(data2)

# Exportar el DataFrame a un archivo Excel
df2.to_excel('datos2.xlsx', index=False)