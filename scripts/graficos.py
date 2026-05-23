"""
Este script toma los datos procesados del archivo 'calculos.py',
los estructura jerárquicamente y genera un gráfico de barras
y líneas con doble eje Y. El resultado se exporta en la caprte 'resultados'.
"""

import os
import matplotlib.pyplot as plt # Librearía para la creación de gráficos y visualizaciones en 2D
import seaborn as sns # Librería para mejorar el diseño, estilos y estética de los gráficos

# Importamos la función calculos para no repetir código
# (Asegúrate de que tu script original se llame 'calculos.py' o cambia el nombre aquí)

from calculos import analizar_partidos

def graficar_rendimiento():
    # 1. Obtenemos los datos procesados del archivo 'calculos.py'
    victorias_dict, prom_goles, tabla_puntos = analizar_partidos()
    
    if tabla_puntos is None:
        print("No se pudieron obtener los datos para graficar.")
        return

    #2. Convertimos los datos a un formato que Matplotlib/Seaborn entiendan fácilmente
    # Ordenamos por puntos para que el gráfico quede jerárquico
    # Usamos sorted con una función lambda que extrae el valor (puntos) para ordenar de mayor a menor (reverse=True)
    equipos_ordenados = sorted(tabla_puntos.items(), key=lambda x: x[1], reverse=True)
    
    # Se separan las claves (equipos) y los valores (puntos) en listas independientes
    equipos = [item[0] for item in equipos_ordenados]
    puntos = [item[1] for item in equipos_ordenados]

    # Buscamos las victorias correspondientes a cada equipo en ese mismo orden
    victorias = [victorias_dict.get(eq, 0) for eq in equipos]

    # 3. Configuración del estilo del gráfico
    # Aplicamos un tema estético limpio de Seaborn con cuadrícula blanca de fondo
    sns.set_theme(style="whitegrid")
    # Inicializamos la figura fijando un tamaño de lienzo proporcional (12 pulgadas de ancho por 8 de alto)
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Gráfico de barras para los Puntos totales
    color_puntos = '#2b5c8f' # Código hexadecimal para azul
    barras = ax1.bar(equipos, puntos, color=color_puntos, alpha=0.8, label='Puntos Totales')

    # Configuración de etiquetas y formato del eje primario (Eje X y Eje Y izquierdo)
    ax1.set_xlabel('Equipos', fontsize=12, fontweight='bold', labelpad=12)
    ax1.set_ylabel('Puntos', color=color_puntos, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_puntos)
    ax1.set_xticklabels(equipos, rotation=45, ha='right', fontsize=10)

    # Añadimos un segundo eje Y para superponer las victorias con una línea
    ax2 = ax1.twinx()
    color_victorias = '#d9534f' # Código hexadecimal para rojo
    
    # Graficamos las victorias en formato de línea continua con marcadores circulares ('o') en cada nodo
    linea = ax2.plot(equipos, victorias, color=color_victorias, marker='o', linewidth=2.5, label='Victorias')
    
    # Configuración de etiquetas del eje secundario (Eje Y derecho)
    ax2.set_ylabel('Cantidad de Victorias', color=color_victorias, fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_victorias)
    ax2.grid(False) # Evitamos que se dupliquen las líneas de la cuadrícula

    # Título y ajustes finales
    plt.title('Comparativa de Rendimiento por Equipo\n(Puntos vs. Victorias Totales)', fontsize=15, fontweight='bold', pad=20)
    fig.tight_layout()

    # 4. Guardar el gráfico en la carpeta "resultados"
    carpeta_resultados = "../resultados"

    # Verificación de directorios: si la carpeta no existe, el script la crea
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)

    # Construcción de la ruta    
    ruta_grafico = os.path.join(carpeta_resultados, "comparativa_rendimiento.png")
    
    # Guardamos el archivo físico definiendo alta densidad de píxeles (dpi=300)
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"¡Gráfico generado con éxito! Guardado en: '{ruta_grafico}'")

# Evita que el código se corra al ser importado
if __name__ == "__main__":
    graficar_rendimiento()
