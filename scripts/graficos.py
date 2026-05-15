#Código que genera gráficos y los guarda
#en la carpeta "resultados"
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Importamos la función calculos para no repetir código
# (Asegúrate de que tu script original se llame 'calculos.py' o cambia el nombre aquí)
#from calculos import analizar_partidos
from calculos import analizar_partidos

def graficar_rendimiento():
    # 1. Obtenemos los datos procesados
    victorias_dict, prom_goles, tabla_puntos = analizar_partidos()
    
    if tabla_puntos is None:
        print("No se pudieron obtener los datos para graficar.")
        return

    #2. Convertimos los datos a un formato que Matplotlib/Seaborn entiendan fácilmente
    # Ordenamos por puntos para que el gráfico quede jerárquico
    equipos_ordenados = sorted(tabla_puntos.items(), key=lambda x: x[1], reverse=True)
    equipos = [item[0] for item in equipos_ordenados]
    puntos = [item[1] for item in equipos_ordenados]
    # Buscamos las victorias correspondientes a cada equipo en ese mismo orden
    victorias = [victorias_dict.get(eq, 0) for eq in equipos]

    # 3. Configuración del estilo del gráfico
    sns.set_theme(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Gráfico de barras para los Puntos totales
    color_puntos = '#2b5c8f'
    barras = ax1.bar(equipos, puntos, color=color_puntos, alpha=0.8, label='Puntos Totales')
    ax1.set_xlabel('Equipos', fontsize=12, fontweight='bold', labelpad=12)
    ax1.set_ylabel('Puntos', color=color_puntos, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_puntos)
    ax1.set_xticklabels(equipos, rotation=45, ha='right', fontsize=10)

    # Añadimos un segundo eje Y para superponer las victorias con una línea
    ax2 = ax1.twinx()
    color_victorias = '#d9534f'
    linea = ax2.plot(equipos, victorias, color=color_victorias, marker='o', linewidth=2.5, label='Victorias')
    ax2.set_ylabel('Cantidad de Victorias', color=color_victorias, fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_victorias)
    ax2.grid(False) # Evitamos que se dupliquen las líneas de la cuadrícula

    # Título y ajustes finales
    plt.title('Comparativa de Rendimiento por Equipo\n(Puntos vs. Victorias Totales)', fontsize=15, fontweight='bold', pad=20)
    fig.tight_layout()

    # 4. Guardar el gráfico en la carpeta "resultados"
    carpeta_resultados = "../resultados"
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)
        
    ruta_grafico = os.path.join(carpeta_resultados, "comparativa_rendimiento.png")
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"¡Gráfico generado con éxito! Guardado en: '{ruta_grafico}'")
    
    # Mostrar en pantalla (ideal para Google Colab)
    plt.show()

if __name__ == "__main__":
    graficar_rendimiento()
