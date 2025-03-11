import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\hecto\Downloads\tarea1\housing.csv')

numeric_cols = ["median_house_value", "population", "total_rooms", "total_bedrooms", "households", "median_income"]

descriptive_stats = pd.DataFrame({
    "Media": df[numeric_cols].mean(),
    "Mediana": df[numeric_cols].median(),
    "Moda": df[numeric_cols].mode().iloc[0],
    "Rango": df[numeric_cols].max() - df[numeric_cols].min(),
    "Varianza": df[numeric_cols].var(),
    "Desviación Estándar": df[numeric_cols].std()
})

def print_table(title, df):
    print("\n" + title)
    print(df.to_string())

print_table("Estadísticas Descriptivas", descriptive_stats)

freq_table = df["median_house_value"].value_counts().sort_index().reset_index()
freq_table.columns = ["Valor de la Vivienda", "Frecuencia"]
print_table("Tabla de Frecuencia de median_house_value", freq_table.head(10))  # Mostramos las primeras 10 filas

mean_house_value = df["median_house_value"].mean()

plt.figure(figsize=(12, 6))
plt.bar(df.index[:20], df["median_house_value"][:20], label="Valor de la Vivienda", alpha=0.7)
plt.bar(df.index[:20], df["population"][:20], label="Población", alpha=0.7)
plt.axhline(mean_house_value, color='red', linestyle='dashed', label="Promedio Valor Vivienda")

plt.xlabel("Índice")
plt.ylabel("Valores")
plt.title("Comparación de Median House Value y Population con su Promedio")
plt.legend()
plt.show()
