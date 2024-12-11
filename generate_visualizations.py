import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
data = pd.read_csv('chernobyl_data.csv')

# Convertir la columna 'Date' a tipo datetime
data['Date'] = pd.to_datetime(data['Date'])

# Crear las visualizaciones
sns.set(style="whitegrid")

# Función para agregar anotaciones
def add_annotations(ax, data):
    for i, row in data.iterrows():
        ax.annotate(f"{row['PAYS']}, {row['Code']}, {row['Ville']}, {row['X']}, {row['Y']}, {row['End of sampling']}, {row['Duration(h.min)']}",
                    (row['Date'], row['I 131 (Bq/m3)']),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center')

# Gráfica 1: Concentración de I-131 a lo largo del tiempo
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Date', y='I 131 (Bq/m3)', data=data)
plt.title('Concentración de I-131 a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Concentración de I-131 (Bq/m3)')
plt.xticks(rotation=45)
plt.tight_layout()
add_annotations(ax, data)
plt.savefig('static/graph1.png')
plt.close()

# Gráfica 2: Concentración de Cs-134 a lo largo del tiempo
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Date', y='Cs 134 (Bq/m3)', data=data)
plt.title('Concentración de Cs-134 a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Concentración de Cs-134 (Bq/m3)')
plt.xticks(rotation=45)
plt.tight_layout()
add_annotations(ax, data)
plt.savefig('static/graph2.png')
plt.close()

# Gráfica 3: Concentración de Cs-137 a lo largo del tiempo
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Date', y='Cs 137 (Bq/m3)', data=data)
plt.title('Concentración de Cs-137 a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Concentración de Cs-137 (Bq/m3)')
plt.xticks(rotation=45)
plt.tight_layout()
add_annotations(ax, data)
plt.savefig('static/graph3.png')
plt.close()

# Gráfica 4: Comparación de concentraciones
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Date', y='I 131 (Bq/m3)', data=data, label='I-131')
sns.lineplot(x='Date', y='Cs 134 (Bq/m3)', data=data, label='Cs-134')
sns.lineplot(x='Date', y='Cs 137 (Bq/m3)', data=data, label='Cs-137')
plt.title('Comparación de concentraciones')
plt.xlabel('Fecha')
plt.ylabel('Concentración (Bq/m3)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
add_annotations(ax, data)
plt.savefig('static/graph4.png')
plt.close()