import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\hecto\Downloads\tarea1\housing.csv')

#Mostrar las 5 primeras filas
print(df.head())

#Ultimas 5 filas
print(df.tail)

#quiero una fila en especifico
print(df.iloc[7])

#Mostrar una columna por su nombre
print(df["ocean_proximity"])

#Quiero obtner la media de la columna de total de cuartos 
mediacuartos = df["total_rooms"].mean()
print('Media cuartoas: ', mediacuartos)

#Quiero obtener la mediana de la columna population
medianapopularidad = df["population"].median()
print('Mediana popularidad: ', medianapopularidad)

std_age = df["housing_median_age"].std()
print('Desviacion Estandar en años', std_age)

#Para filtrar
filtrodeloceano = df[df["ocean_proximity"] == "ISLAND"]
print("Filtro de proximidad del oceano: ", filtrodeloceano)

#vamos a crear un grafico de dispersion entre los registros de la proximidad del oceano vslos precios
plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

#Hay que definir a x y
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title("Grafico de Dispersion de Proximidad al Oceano vs Precio")
plt.show()