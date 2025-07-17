'''
Acerca del desafío 💡
Descripción

Telecom X - Análisis de Evasión de Clientes
Has sido contratado como asistente de análisis de datos en Telecom X y formarás parte del proyecto "Churn de Clientes". La empresa enfrenta una alta tasa de cancelaciones y necesita comprender los factores que llevan a la pérdida de clientes.

Tu desafío será recopilar, procesar y analizar los datos, utilizando Python y sus principales bibliotecas para extraer información valiosa. A partir de tu análisis, el equipo de Data Science podrá avanzar en modelos predictivos y desarrollar estrategias para reducir la evasión.

¿Qué vas a practicar? ✅ Importar y manipular datos desde una API de manera eficiente. ✅ Aplicar los conceptos de ETL (Extracción, Transformación y Carga) en la preparación de los datos. ✅ Crear visualizaciones estratégicas para identificar patrones y tendencias. ✅ Realizar un Análisis Exploratorio de Datos (EDA) y generar un informe con insights relevantes.

¡Ahora es tu turno! 🚀 Usa tus conocimientos para transformar datos en información estratégica y ayudar a Telecom X a retener más clientes.

1-Extracción de datos:
Descripción Para iniciar tu análisis, necesitarás importar los datos de la API de Telecom X. Estos datos están disponibles en formato JSON y contienen información esencial sobre los clientes, incluyendo datos demográficos, tipo de servicio contratado y estado de evasión.

📌 Enlace de la API: 🔗 challenge2-data-science-LATAM/TelecomX_Data.json at main · ingridcristh/challenge2-data-science-LATAM

🔗GitHub - ingridcristh/challenge2-data-science-LATAM

¿Qué debes hacer? ✅ Cargar los datos directamente desde la API utilizando Python. ✅ Convertir los datos a un DataFrame de Pandas para facilitar su manipulación.

Este es el primer paso para transformar los datos en información valiosa. ¿Listo para programar? 🚀

2 - Conoce el conjunto de datos
Descripción Ahora que has extraído los datos, es fundamental comprender la estructura del dataset y el significado de sus columnas. Esta etapa te ayudará a identificar qué variables son más relevantes para el análisis de evasión de clientes.

📌 Para facilitar este proceso, hemos creado un diccionario de datos con la descripción de cada columna. Aunque no es obligatorio utilizarlo, puede ayudarte a comprender mejor la información disponible.

🔗 Enlace al diccionario y a la API

¿Qué debes hacer? ✅ Explorar las columnas del dataset y verificar sus tipos de datos. ✅ Consultar el diccionario para comprender mejor el significado de las variables. ✅ Identificar las columnas más relevantes para el análisis de evasión.

📌 Tips: 🔗 Documentación de DataFrame.info() 🔗 Documentación de DataFrame.dtypes

3 - Comprobación de incoherencias en los datos
Descripción En este paso, verifica si hay problemas en los datos que puedan afectar el análisis. Presta atención a valores ausentes, duplicados, errores de formato e inconsistencias en las categorías. Este proceso es esencial para asegurarte de que los datos estén listos para las siguientes etapas.

📌 Tips:

🔗 Documentación de pandas.unique() 🔗 Documentación de pandas.Series.dt.normalize()

4 - Manejo de inconsistencias
Descripción Ahora que has identificado las inconsistencias, es momento de aplicar las correcciones necesarias. Ajusta los datos para asegurarte de que estén completos y coherentes, preparándolos para las siguientes etapas del análisis.

📌 Tips:

🔗 Manipulación de strings en pandas: lower, replace, startswith y contains | Alura Cursos Online

5 - Columna de cuentas diarias
Descripción Ahora que los datos están limpios, es momento de crear la columna "Cuentas_Diarias". Utiliza la facturación mensual para calcular el valor diario, proporcionando una visión más detallada del comportamiento de los clientes a lo largo del tiempo.

📌 Esta columna te ayudará a profundizar en el análisis y a obtener información valiosa para las siguientes etapas.

6 - Estandarización y transformación de datos (opcional)
Descripción La estandarización y transformación de datos es una etapa opcional, pero altamente recomendada, ya que busca hacer que la información sea más consistente, comprensible y adecuada para el análisis. Durante esta fase, por ejemplo, puedes convertir valores textuales como "Sí" y "No" en valores binarios (1 y 0), lo que facilita el procesamiento matemático y la aplicación de modelos analíticos.

Además, traducir o renombrar columnas y datos hace que la información sea más accesible y fácil de entender, especialmente cuando se trabaja con fuentes externas o términos técnicos. Aunque no es un paso obligatorio, puede mejorar significativamente la claridad y comunicación de los resultados, facilitando la interpretación y evitando confusiones, especialmente al compartir información con stakeholders no técnicos.

7 - Carga y análisis(L - Load & Analysis)
Análisis Descriptivo
Descripción Para comenzar, realiza un análisis descriptivo de los datos, calculando métricas como media, mediana, desviación estándar y otras medidas que ayuden a comprender mejor la distribución y el comportamiento de los clientes.

📌 Consejos:

🔗 Documentación de DataFrame.describe()

8 - Distribución de evasión
Descripción En este paso, el objetivo es comprender cómo está distribuida la variable "churn" (evasión) entre los clientes. Utiliza gráficos para visualizar la proporción de clientes que permanecieron y los que se dieron de baja.

9 - Recuento de evasión por variables categóricas
Descripción Ahora, exploraremos cómo se distribuye la evasión según variables categóricas, como género, tipo de contrato, método de pago, entre otras.

Este análisis puede revelar patrones interesantes, por ejemplo, si los clientes de ciertos perfiles tienen una mayor tendencia a cancelar el servicio, lo que ayudará a orientar acciones estratégicas.

10 - Conteo de evasión por variables numéricas
Descripción En este paso, explora cómo las variables numéricas, como "total gastado" o "tiempo de contrato", se distribuyen entre los clientes que cancelaron (evasión) y los que no cancelaron.

Este análisis ayuda a entender si ciertos valores numéricos están más asociados con la evasión, proporcionando insights sobre los factores que influyen en el comportamiento de los clientes.

11 - Informe final
Descripción Finaliza el desafío elaborando un informe dentro del mismo notebook que resuma todo el trabajo realizado. El informe debe incluir:

🔹 Introducción: Explica el objetivo del análisis y el problema de evasión de clientes (Churn).

🔹 Limpieza y Tratamiento de Datos: Describe los pasos realizados para importar, limpiar y procesar los datos.

🔹 Análisis Exploratorio de Datos: Presenta los análisis realizados, incluyendo gráficos y visualizaciones para identificar patrones.

🔹 Conclusiones e Insights: Resume los principales hallazgos y cómo estos datos pueden ayudar a reducir la evasión.

🔹 Recomendaciones: Ofrece sugerencias estratégicas basadas en tu análisis.

Asegúrate de que el informe esté bien estructurado, claro y respaldado por visualizaciones que refuercen tus conclusiones. 🚀

12 - ¡Extra! Análisis de correlación entre variables
Descripción Esta actividad es un extra, por lo tanto es OPCIONAL.

Como un paso adicional, puedes explorar la correlación entre diferentes variables del dataset. Esto puede ayudar a identificar qué factores tienen mayor relación con la evasión de clientes, como:

🔹 La relación entre la cuenta diaria y la evasión. 🔹 Cómo la cantidad de servicios contratados afecta la probabilidad de churn.

Puedes usar la función corr() de Pandas para calcular las correlaciones y visualizar los resultados con gráficos de dispersión o matrices de correlación.

Este análisis adicional puede proporcionar insights valiosos para la creación de modelos predictivos más robustos. 🚀
'''

import pandas as pd
import requests
import io

# Paso 1: Extracción de datos
# URL del archivo JSON en GitHub (raw)
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"

# Descargar el contenido del archivo JSON
response = requests.get(url)
response.raise_for_status()  # Asegura que la descarga fue exitosa

# Cargar los datos en un DataFrame de pandas
data = pd.read_json(io.StringIO(response.text))

# Mostrar las primeras filas para verificar la carga
print("Primeras filas del DataFrame:")
print(data.head())

# Paso 2: Conocer el conjunto de datos
print("\nInformación general del DataFrame:")
data.info()

print("\nTipos de datos por columna:")
print(data.dtypes)

print("\nColumnas del DataFrame:")
print(data.columns.tolist())

'''
Primeras filas del DataFrame:
   customerID  ...                                            account
0  0002-ORFBO  ...  {'Contract': 'One year', 'PaperlessBilling': '...
1  0003-MKNFE  ...  {'Contract': 'Month-to-month', 'PaperlessBilli...
2  0004-TLHLJ  ...  {'Contract': 'Month-to-month', 'PaperlessBilli...
3  0011-IGKFF  ...  {'Contract': 'Month-to-month', 'PaperlessBilli...
4  0013-EXCHZ  ...  {'Contract': 'Month-to-month', 'PaperlessBilli...

[5 rows x 6 columns]

Información general del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7267 entries, 0 to 7266
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   customerID  7267 non-null   object
 1   Churn       7267 non-null   object
 2   customer    7267 non-null   object
 3   phone       7267 non-null   object
 4   internet    7267 non-null   object
 5   account     7267 non-null   object
dtypes: object(6)
memory usage: 340.8+ KB

Tipos de datos por columna:
customerID    object
Churn         object
customer      object
phone         object
internet      object
account       object
dtype: object




¡Perfecto! Tienes un roadmap claro para abordar el desafío de análisis de churn en Telecom X. Aquí tienes una guía paso a paso para avanzar, con sugerencias de código y enfoques para cada etapa:

1. Extracción de datos
Ya lo tienes hecho: descargaste y cargaste el JSON en un DataFrame.

2. Conoce el conjunto de datos
Ya mostraste las columnas y tipos de datos.
Siguiente paso: Explora el contenido de las columnas anidadas (customer, phone, internet, account), ya que parecen ser diccionarios.

'''
# Ejemplo: ver el contenido de la columna 'customer' en la primera fila
print(data['customer'][0])

'''
Columnas del DataFrame:
['customerID', 'Churn', 'customer', 'phone', 'internet', 'account']
{'gender': 'Female', 'SeniorCitizen': 0, 'Partner': 'Yes', 'Dependents': 'Yes', 'tenure': 9}
'''

'''
3. Comprobación de incoherencias en los datos
Busca valores nulos, duplicados y categorías extrañas.
'''
# Expandir la columna 'account' en columnas separadas
account_df = pd.json_normalize(data['account'])
# Unir al DataFrame original
data = pd.concat([data.drop('account', axis=1), account_df], axis=1)

for col in ['customer', 'phone', 'internet']:
    expanded = pd.json_normalize(data[col])
    expanded.columns = [f"{col}_{subcol}" for subcol in expanded.columns]
    data = pd.concat([data.drop(col, axis=1), expanded], axis=1)
'''

'''
print(data.isnull().sum())  # Valores nulos por columna
print(data.duplicated().sum())  # Filas duplicadas



# Ejemplo para ver valores únicos en 'Churn'
print(data['Churn'].unique())

'''
customerID                   0
Churn                        0
Contract                     0
PaperlessBilling             0
PaymentMethod                0
Charges.Monthly              0
Charges.Total                0
customer_gender              0
customer_SeniorCitizen       0
customer_Partner             0
customer_Dependents          0
customer_tenure              0
phone_PhoneService           0
phone_MultipleLines          0
internet_InternetService     0
internet_OnlineSecurity      0
internet_OnlineBackup        0
internet_DeviceProtection    0
internet_TechSupport         0
internet_StreamingTV         0
internet_StreamingMovies     0
dtype: int64
0
['No' 'Yes' '']
'''
'''
¡Perfecto! Ya tienes el diagnóstico: tus columnas anidadas (customer, phone, internet, account) contienen diccionarios, y ya has visto un ejemplo de su contenido.
Siguiente paso: Desanidar todas las columnas de diccionarios
Esto te permitirá:
Analizar fácilmente los valores únicos, nulos, duplicados, etc.
Trabajar con un DataFrame "plano" y listo para análisis y visualización.
Código recomendado para desanidar todas las columnas anidadas
Agrega esto después de cargar el DataFrame y antes de cualquier análisis:


'''
cols_to_expand = ['customer', 'phone', 'internet', 'account']

for col in cols_to_expand:
    if col in data.columns:
        expanded = pd.json_normalize(data[col])
        expanded.columns = [f"{col}_{subcol}" for subcol in expanded.columns]
        data = pd.concat([data.drop(col, axis=1), expanded], axis=1)

'''
¡Genial! Ya tienes tu DataFrame completamente desanidado y plano, con columnas limpias y listas para el análisis. Aquí tienes los siguientes pasos recomendados para avanzar en el desafío:
1. Revisión de valores nulos, duplicados y categorías
Ya lo hiciste, pero asegúrate de revisar las nuevas columnas expandidas. Si todo está en orden (como parece por tu salida), ¡puedes avanzar!
2. Limpieza y estandarización de datos
Estandariza los valores de las columnas categóricas (por ejemplo, "Yes"/"No" a 1/0).
Reemplaza valores vacíos o inconsistentes (por ejemplo, si hay valores '' en vez de NaN).
Ejemplo:
'''
# Estandarizar columnas Yes/No
yes_no_cols = [col for col in data.columns if data[col].isin(['Yes', 'No']).all()]
for col in yes_no_cols:
    data[col] = data[col].map({'Yes': 1, 'No': 0})

# Reemplazar strings vacíos por NaN
import numpy as np
data.replace('', np.nan, inplace=True)

'''
3. Crear columna de cuentas diarias
Si tienes la columna Charges.Monthly, crea la columna Cuentas_Diarias:

'''
data['Cuentas_Diarias'] = data['Charges.Monthly'] / 30

'''
4. Análisis descriptivo
Usa describe() para ver estadísticas de las columnas numéricas.
Usa value_counts() para ver la distribución de las categóricas.
5. Visualización de la evasión (Churn)
Haz un gráfico de torta o barras para la variable Churn.
Ejemplo:
'''

import matplotlib.pyplot as plt
data['Churn'].value_counts().plot(kind='bar')
plt.title('Distribución de Evasión (Churn)')
plt.show()

'''
6. Análisis de churn por variables relevantes
Usa tablas cruzadas y gráficos para ver cómo se distribuye el churn según género, tipo de contrato, método de pago, etc.
Ejemplo
'''

pd.crosstab(data['Churn'], data['Contract']).plot(kind='bar', stacked=True)
plt.title('Churn por tipo de contrato')
plt.show()
'''
7. Análisis de churn por variables numéricas
Compara medias, medianas, etc., de Charges.Total, Cuentas_Diarias, tenure, etc., entre clientes que se fueron y los que no.
8. (Opcional) Análisis de correlación
Usa data.corr() y un heatmap para ver correlaciones entre variables numéricas y el churn.
9. Informe final
Estructura tu notebook/script con:
Introducción
Limpieza y tratamiento
Análisis exploratorio (con visualizaciones)
Conclusiones e insights
Recomendaciones
'''
