#!/home/juan/anaconda3/bin/python3.11
'''
    Scripts para el análisis estadístico de los datos para el proyecto de IE0405
'''

# Importación de los datos
# Libreria Pandas
import pandas as pd
# Ajuste de Matplotlib
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'

# Importanción del archivo .csv
musica = pd.read_csv('tcc_ceds_music.csv')

valores_loud = []

for index, row in musica.iterrows():
    if (0 <= row["loudness"] <= 0.333):
        valores_loud.append("low")
    elif (0.333 < row["loudness"] < 0.666):
        valores_loud.append("mid")
    else:
        valores_loud.append("high")

categorical_loudness = pd.DataFrame({"categorical_loudness": valores_loud})


#print(musica["loudness"].between(0, 0.333, inclusive="both").value_counts())
#print(musica["loudness"].between(0.333, 0.666, inclusive="neither").value_counts())
#print(musica["loudness"].between(0.666, 1, inclusive="both").value_counts())

musica = musica.join(categorical_loudness)

print(musica["categorical_loudness"])
