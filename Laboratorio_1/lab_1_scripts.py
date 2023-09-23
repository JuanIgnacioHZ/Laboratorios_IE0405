#!/home/juan/anaconda3/bin/python3.11
'''
    Scripts para análisis estadístico de los datos para el proyecto de IE0405
'''

# Importación de los datos
# Libreria Pandas
import pandas as pd
# Ajuste de Matplotlib
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'


# Declaración de funciones
def agregar_volumen_categorico(dataframe):
    '''
        Esta función se encarga de categorizar los valores de volumen y
    agregarlos como una columna extra al data frame que se ingresa
    '''
    valores_vol = []    # Valores vol = loudness values

    for index, row in dataframe.iterrows():
        if 0 <= row["loudness"] <= 0.333:
            valores_vol.append("low")
        elif 0.333 < row["loudness"] < 0.666:
            valores_vol.append("mid")
        else:
            valores_vol.append("high")

    categorical_loudness = pd.DataFrame({"categorical_loudness": valores_vol})


    #print(dataframe["loudness"].between(0, 0.333, inclusive="both").value_counts())
    #print(dataframe["loudness"].between(0.333, 0.666, inclusive="neither").value_counts())
    #print(dataframe["loudness"].between(0.666, 1, inclusive="both").value_counts())

    dataframe = dataframe.join(categorical_loudness)

    return dataframe


def obtener_frecuencias_relativas(dataframe):
    '''
        Se encarga de obtener las frecuencias relativas para las variables
    categóricas en estudio
    '''

    # Cantidad total de canciones
    cant_canciones = len(dataframe.index)

    # Columnas a estudiar
    variables_categoricas = ['categorical_loudness', 'genre', 'topic']

    # Variable de salida
    frecuencias = {}

    # Se recorren las variables categóricas para obtener su frecuencia relativa
    for i in variables_categoricas:
        dict_tmp = {}   # Variable temporal
        # Luego, se recorre la cantidad de elementos de cada columna para
        # obtener su frecuencia relativa
        for j, k in dataframe[i].value_counts().items():
            # El formato de los datos es el siguiente:
            # "nombre de categoría" = frecuencia relativa
            dict_tmp[j] = k/cant_canciones
        frecuencias[i] = dict_tmp

    return frecuencias


# Importanción del archivo .csv
musica = agregar_volumen_categorico(pd.read_csv('tcc_ceds_music.csv'))

# Declaración de variables
frec_relativas = obtener_frecuencias_relativas(musica)

