import numpy as np
from scipy.stats import norm
import pandas as pd

# Datos sobre la simulación 
dolar = 16.83                       # Valor del dolar de hoy
n_conferencistas = int(input("Cuantos conferencistas asistiran: "))
conferencistas = 2000 * dolar * n_conferencistas
equipo_sonido = 50000
n_invitados = int(input("\nCuantos invitados asistiran: "))
porcentaje_Ganacia = np.random.uniform(0.10,0.15)
invitados = 1800 * dolar * n_invitados
renta_espacio = 0 
a = 30000                           #Limite inferior
b = 50000                           #limite superior
#uniforme = equipo_sonido + np.random.uniform(a, b)
asistentes_L1 = 2000
asistentes_L2 = 4800

prediccion_costos = []
prediccion_asistencia = []
asistencia_lugar1 = []
n = 1000

# Calculo de los asistentes, sifue una distribución normal
def asistencia(n, a, b): 
    numeros_normalizados = []
    media = (a + b)/2
    desviacion = 3
    u_lista = []
    z = []
    for i in range(n):
        u = np.random.uniform(0,1)
        u_lista.append(UserWarning)
        z1 = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * u)
        z2 = np.sqrt(-2 * np.log(u)) * np.sin(2 * np.pi * u)
        z.append(z1)
        # Ajustar los valores generados al rango deseado
        numeros_normalizados.append(z1 * desviacion + media)
        
    # Crear un DataFrame de pandas
    data2 = {'Aletorio1':u_lista, 'z':z,'Asistencia': numeros_normalizados}
    df2 = pd.DataFrame(data2)
    df2.to_excel('datos1.xlsx', index=False)
    
    return np.clip(numeros_normalizados, a, b)

# Calculo de los gastos 
def gastos(n):
    u = []
    prediccion_costos = []
    for i in range(n):
        uniforme = equipo_sonido + np.random.uniform(a, b)
        u.append(uniforme)
        prediccion_costos.append(uniforme + conferencistas + invitados + renta_espacio)
    
    data2 = {'Aletorio1':u, 'Gastos':prediccion_costos}
    df2 = pd.DataFrame(data2)
    df2.to_excel('datos2.xlsx', index=False)

    return prediccion_costos

# Asistentes que van de lugar 1 al 2
def inteseccion(n,asistencia_lugar1):
    prediccion = []
    u = []
    for i in range(n):
        porcentaje_Lugar1y2 = np.random.uniform(0.15,0.30)
        u.append(porcentaje_Lugar1y2)
        prediccion.append(asistencia_lugar1 * porcentaje_Lugar1y2)
    
    data2 = {'Aletorio1':u, 'asistencia':prediccion}
    df2 = pd.DataFrame(data2)
    df2.to_excel('datos3.xlsx', index=False)

    return prediccion

#------------------------------------------------------------------------
# Llamamos a la funcion de gastos
prediccion_costos = gastos(n)

# Llamo ala funcion asistencia 
prediccion_asistencia = asistencia(n, 80, 100)

media_costos = sum(prediccion_costos)/n
media_asistencia = (np.mean(prediccion_asistencia) / 100) * (asistentes_L1 + asistentes_L2)
asistencia_inteseccion = (np.mean(asistencia_lugar1) / 100) * asistentes_L1 

print("\nRESULTADO de SIMULACION")
print("\nMedia de costos: ", media_costos)
print("\nMedia de asistencia: ",media_asistencia)

costo_boleto = media_costos / media_asistencia
print("\nCosto de boletos con cero de ganacia: ", costo_boleto)

#--------------------------------------------------------------
# Porcentaje de ganacia con ganacias de 10 al 15 %
precio_nuevo = (1 + porcentaje_Ganacia) * costo_boleto 
print("\nGanacias con el ",porcentaje_Ganacia * 100," porciento son:", precio_nuevo)

#-------------------------------------------------------------------
"""# Interseccion entre las personas que van del lufar 1 al 2 
asistencia_lugar1 = (np.mean(asistencia(n, 80, 100)) / 100) * asistentes_L1
# Llamamos a la funcion de interseccion
interseccion_lugar1y2 = inteseccion(n, asistencia_lugar1)
print("\nInteseccion de que las personas que esten en el lugar 1 y vayan a lugar 2 es: ", (np.mean(interseccion_lugar1y2)) ) 

#------------------------------------------------------------------
# Escenario pesimista y media
# Media
prediccion_costos = gastos(n)
escenario_media = asistencia(n, 50, 70)
escenario_media = (np.mean(escenario_media) / 100) * (asistentes_L1 + asistentes_L2)
media_costos = np.mean(prediccion_costos)
costo_boleto = media_costos / escenario_media
print("\nCosto de boletos con escenario media (50-70) : ", costo_boleto)

# Pesimista
prediccion_costos = gastos(n)
escenario_pesimista = (np.mean(asistencia(n, 30, 50)) / 100) * (asistentes_L1 + asistentes_L2)
media_costos = np.mean(prediccion_costos) 
costo_boleto = media_costos / escenario_pesimista
print("\nCosto de boletos con escenario pesimista (30-50) : ", costo_boleto)
"""
  