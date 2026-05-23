# estadisticas_deportivas

## Descripción
Análisis estadístico correspondientes a resultados del campeonato de la liga profesional de fútbol argentino, con el objetivo de procesar los resultados de los partidos para generar estadísticas básicas del torneo.

## Equipo
* **P1 - Juan Manuel Reyes Lima:** Líder y Organizador
* **P2 - Carolina Rodríguez:** Desarrollador Técnico
* **P3 - Juan Manuel Reyes Lima:** Revisor y QA

## Estructura del proyecto
* /scripts → Carpeta que contiene los scripts de análisis en Python
* /datos → Carpeta que contiene el archivo dataset 'ARG.csv'
* /resultados → Carpeta que almacena los reportes de texto (.txt) y las imágenes (.png)

## Fuente de datos
Dataset obtenido de https://www.football-data.co.uk/argentina.php

## Características
El sistema procesa el archivo de datos y extrae de forma automática:
1.  Ranking de Victorias: cantidad de partidos ganados por equipo.
2.  Tabla de Posiciones: cantidad de puntos totales (3 por victoria, 1 por empate).
3.  Promedio de Goles: promedio de goles por partido.
4.  Visualización Mixta: un gráfico de doble eje Y que contrasta los puntos totales obtenidos frente a la cantidad de victorias por cada club.

## Cómo ejecutar el proyecto
Para correr el proyecto en entornos locales o Google Colab, asegúrate de tener instaladas las dependencias pandas, matplotlib y seaborn.
Podés instalar todas las librerías, ejecutando en tu terminal de Google Colab este comando:
* pip install pandas matplotlib seaborn

Una vez verificado que las librerías están instaladas, clonar el repositorio ejecutando:
* !git clone https://github.com/Estadisticas-deportivas/estadisticas_deportivas.git

Luego cambiar al directorio /scripts
* %cd estadisticas_deportivas/scripts

Por último, para realizar los cálculos:
* !python calculos.py
Y para crear los gráficos:
* !python graficos.py

## Aclaración importante!! 
El programa que realiza los gráficos utiliza las funciones y los resultados que realiza el programa cálculos.py, con lo cual este debe ser ejecutado primero.