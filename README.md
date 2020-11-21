
# Linea Python y DS
## Reto: CSV's y filtrado de datos
### Descripción:
Ahora que conocemos las estructuras de datos mas comunes para realizar manejo de datos en python (Dataframes)
vamos a realizar una tarea que es muy común en el area de DS, la cual es la lectura de archivos CSV.

Los archivos CSV son archivos de texto plano que buscan representar tablas de datos en las cuales son valores están 
separados por comas. (CSV: Comma-separated values) Aquí un pequeño ejemplo:
```text
adult, belongs_to_collection, budget, id, imdb_id, original_language,original_title
False, Toy Story Collection, 30000000, 862, tt0114709, en, Toy Story
False, James Bond Collection, 58000000, 710, tt0113189, en, GoldenEye
...
```

### Objetivo:
Completar la función `analizar_peliculas` para que lea el archivo CSV llamado `movies_metadata.csv` que se encuentra en 
la carpeta. Este archivo lo tenemos que cargar en un Dataframe usando python, nos podemos ayudar de la librería `pandas` 
para ello (Consulta como leer un archivo CSV usando pandas en caso de que sea necesario). 

El archivo original de `movies_metadata.csv` contiene las siguientes columnas:
- adult
- belongs_to_collection
- budget
- genres
- homepage
- id
- imdb_id
- original_language
- original_title
- overview
- popularity
- poster_path
- production_companies
- production_countries
- release_date
- revenue
- runtime
- spoken_languages
- status
- tagline
- title
- video
- vote_average
- vote_count

El objetivo es extraer un nuevo Dataframe con las siguientes características:
   1. El nuevo Dataframe solo debe contener estas columnas:
       - title
       - release_date
       - budget 
       - revenue
       - runtime
   2. Las películas que cumplan todas las siguientes condiciones:
       - Hayan generado un **retorno** (revenue) de mas de **2000000** USD
       - Su **presupuesto** (budget) haya sido inferior a **1000000** USD
       
Puedes investigar como filtrar Dataframes en python para solucionar el segundo item.
   
##### Input: 
Un archivo CSV con un dataset de películas
#### Output:
Un nuevo Dataframe solo con los datos que cumplen las características mencionadas
### Preparación entorno:
Antes de comenzar con el reto es importante que instalemos las librerías que vamos a usar. Para esto haremos uso del 
siguiente comando:
```shell script
$ pip install -r requirements.txt
```


### Comprobar resultados:
Para comprobar los resultados puedes ejecutar el script main.py usando:
```shell script
$ python main.py
```
Y deberías de ver los siguiente:
```shell script
Excelente, has aprendido a leer CSV's con python y como filtrarlos!
```