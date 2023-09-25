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
def agregar_bailabilidad_categorica(dataframe):
    '''
        Esta función se encarga de categorizar los valores de bailabilidad y
    agregarlos como una columna extra al data frame que se ingresa
    '''
    # Se asume que las canciones tienen una distribución normal en su caracteristica
    # de que tan bailable es
    # Cálculo de la media y desviación estandar
    media = dataframe['danceability'].mean()

    valores_bail = []    # Valores bail = danceability value

    for index, row in dataframe.iterrows():
        if 0 <= row['danceability'] <= media:
            valores_bail.append("undanceable")
        else:
            valores_bail.append("danceable")

    categorical_danceability = pd.DataFrame({"categorical_danceability":
                                             valores_bail})

    dataframe = dataframe.join(categorical_danceability)

    return dataframe


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

    dataframe = dataframe.join(categorical_loudness)

    return dataframe


def obtener_frecuencias_relativas(dataframe):
    '''
        Se encarga de obtener las frecuencias relativas para las variables
    categóricas en estudio
    '''
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


def generar_graficos(dataframe):
    '''
        Esta función se encarga de generar los histogramas presentados en
    la presentación del proyecto y salvarlos como .svg
    '''
    # Datos de los que sacar los histogramas para las variables categóricas
    # y numéricas por aparte
    graficas_cat = ['categorical_loudness',
                    'categorical_danceability',
                    'genre',
                    'topic']
    etiqueta_eje_x_hist_cat = ['Nivel de volumen',
                               'Bailabilidad',
                               'Género',
                               'Tema central']

    histograma_num = ['loudness',
                      'danceability']
    etiqueta_eje_x_hist_num = ['Nivel de volumen',
                               'Bailabilidad']

    # Se recorre el DataFrame para exportar las gráficas de variables
    # categóricas
    for i in range(len(graficas_cat)):
        # Datos temporales
        datos_tmp = dataframe[graficas_cat[i]].value_counts()
        # Gráfica de matplotlib
        plt.bar(datos_tmp.index, datos_tmp.values)
        plt.xlabel(etiqueta_eje_x_hist_cat[i])
        plt.ylabel('Cantidad de canciones')
        plt.savefig(str('img/' +
                        graficas_cat[i] +
                        '_graph.svg'),
                    transparent=True)
        plt.clf()   # Limpia la última figura creada en memoria memoria

    # Y sucede lo mismo con la gráfica de valores numéricos
    for i in range(len(histograma_num)):
        plt.hist(dataframe[histograma_num[i]], bins=10)
        plt.xlabel(etiqueta_eje_x_hist_num[i])
        plt.ylabel('Cantidad de canciones')
        plt.savefig(str('img/' +
                        histograma_num[i] +
                        '_graph.svg'),
                    transparent=True)
        plt.clf()   # Limpia la última figura creada en memoria memoria
    
    # Con esto, ya todas las gráficas han sido generadas


def exportar_ejemplo(dataframe):
    '''
        Exporta dos muestras de datos del dataframe y los salva en un
    archivo html
    '''
    musica.sample(n=2, random_state=1).to_html('datos_ejemplo.html')


# Importanción del archivo .csv
musica = agregar_volumen_categorico(pd.read_csv('tcc_ceds_music.csv'))

# Y sucede lo mismo con la bailabilidad
musica = agregar_bailabilidad_categorica(musica)

# Cantidad total de canciones
global cant_canciones
cant_canciones = len(musica.index)

# Declaración de variables
frec_relativas = obtener_frecuencias_relativas(musica)

# Se generan las gráficas de interés en la presentación
generar_graficos(musica)

# Se exportan los datos a usar de ejemplo en la presentación
exportar_ejemplo(musica)

# Problema 1, probabilidad clásica
prob_tristeza = frec_relativas['topic']['sadness']
prob_jazz = frec_relativas['genre']['jazz']

# Problema 2, probabilidad condicional
# Caso 1 Violencia & Volumen alto
violencia_and_vol_alto = musica[(musica['topic'] == 'violence') &
                           (musica['categorical_loudness'] == 'high')]
prob_violencia_and_vol_alto = len(violencia_and_vol_alto)/cant_canciones
# Caso 2 Hable de tristeza & Pop
tristeza_and_pop = musica[(musica['topic'] == 'sadness') &
                           (musica['genre'] == 'pop')]
prob_tristeza_and_pop = len(tristeza_and_pop)/cant_canciones


print("prob_violencia_and_vol_alto:\t{0:1.5}".format(prob_violencia_and_vol_alto))
print("prob_tristeza_and_pop:\t{0:1.5}".format(prob_tristeza_and_pop))

print("prob_tristeza:\t{0:1.5}".format(prob_tristeza))
print("prob_jazz:\t{0:1.5}".format(prob_jazz))



#print(frec_relativas)

