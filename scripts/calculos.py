#Código que calcula el ranking por equipos,
#promedio de goles por partido y tabla de posiciones.
#Los resultados se generarán en archivos .txt y se guardarán
#en la carpeta "resultados"


import pandas as pd # Librería para manejar archivos .csv
import os 

# ==========================================
# 1. RANKING DE VICTORIAS
# ==========================================
def analizar_partidos():
    """
    Lee los datos del archivo CSV de partidos, calcula las estadísticas
    de victorias, promedio de goles generales y genera la tabla de posiciones.

    Devuelve:
        diccionario de victorias, el promedio de goles y diccionario puntos de equipos 
        si la lectura es exitosa.
        (None, None, None) si ocurre algún error de E/S o de formato.
    """
    ruta = os.path.join("../datos", "ARG.csv")
    #ruta = os.path.join("ARG.csv")

    try:
        # Carga del dataset original
        df = pd.read_csv(ruta) 
        # Extracción de columnas críticas mediante indexación numérica (.iloc)
        # Nota de QA: Índices mapeados en base 0 (Columnas 6 a 10 del archivo real)
        equipos_local = df.iloc[:, 5]
        equipos_visita = df.iloc[:, 6]
        goles_local = df.iloc[:, 7]
        goles_visita = df.iloc[:, 8]
        resultados = df.iloc[:, 9]

        # ===========================================
        # 1. RANKING DE VICTORIAS
        # ===========================================
        # Frecuencia de victorias locales ('H' - Home) y visitantes ('A' - Away)
        ganados_local = equipos_local[resultados == 'H'].value_counts()
        ganados_visita = equipos_visita[resultados == 'A'].value_counts()

        # Sumamos ambos resultados para tener el total de victorias por equipo
        # .add() combina las series y fill_value=0 evita errores si un equipo nunca ganó de visita
        total_victorias = ganados_local.add(ganados_visita, fill_value=0).astype(int)

        # Convertimos la Serie de Pandas a un diccionario estándar de Python
        victorias = total_victorias.to_dict()

        # ==========================================
        # 2. PROMEDIO DE GOLES
        # ==========================================
        total_goles = goles_local.sum() + goles_visita.sum()
        total_partidos = len(df)
        promedio_goles = total_goles / total_partidos if total_partidos > 0 else 0

        # ==========================================
        # 3. TABLA DE POSICIONES
        # ==========================================
        # Creamos un diccionario para acumular los puntos de cada equipo
        puntos_equipos = {}

        # Inicializamos todos los equipos con 0 puntos para evitar que falte alguno
        todos_los_equipos = pd.concat([equipos_local, equipos_visita]).unique()
        for eq in todos_los_equipos:
            puntos_equipos[eq] = 0

        # Calculamos los puntos según el resultado
        for i, res in enumerate(resultados):
            loc = equipos_local.iloc[i]
            vis = equipos_visita.iloc[i]
            
            if res == 'H':    # Gana Local
                puntos_equipos[loc] += 3
            elif res == 'A':  # Gana Visitante
                puntos_equipos[vis] += 3
            elif res == 'D':  # Empate
                puntos_equipos[loc] += 1
                puntos_equipos[vis] += 1

        return victorias, promedio_goles, puntos_equipos
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None, None, None

def mostrar_ranking(diccionario):
    # formato de la tabla
    print(f"\n{'Equipo':<25} | {'Ganados'}")
    print("-" * 35)
    
    # Ordenamos el diccionario por sus valores (victorias) de mayor a menor
    items_ordenados = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
    
    for equipo, ganados in items_ordenados:
        #formato del resultado
        print(f"{equipo:<25} | {ganados}")

def mostrar_tabla_posiciones(puntos_dict):
    # formato de la tabla
    print(f"\n{'Pos':<4} | {'Equipo':<25} | {'Puntos'}")
    print("-" * 40)
    
    # Ordenamos de mayor a menor cantidad de puntos
    tabla_ordenada = sorted(puntos_dict.items(), key=lambda x: x[1], reverse=True)
    
    for i, (equipo, puntos) in enumerate(tabla_ordenada, start=1):
        print(f"{i:<4} | {equipo:<25} | {puntos}")

# ==========================================
# FUNCIONES PARA GUARDAR EN ARCHIVOS
# ==========================================
def guardar_ranking(diccionario, carpeta):
    # Genera el reporte txt del ranking de victorias
    ruta_archivo = os.path.join(carpeta, "ranking_victorias.txt")
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("=== RANKING DE VICTORIAS ===\n\n")
        f.write(f"{'Equipo':<25} | {'Ganados'}\n")
        f.write("-" * 35 + "\n")
        
        items_ordenados = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
        for equipo, ganados in items_ordenados:
            f.write(f"{equipo:<25} | {ganados}\n")

def guardar_estadisticas(promedio_goles, carpeta):
  # Genera el reporte txt de la liga por promedio de goles.
    ruta_archivo = os.path.join(carpeta, "estadisticas_generales.txt")
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("=== ESTADÍSTICAS GENERALES ===\n\n")
        f.write(f"Promedio de goles por partido: {promedio_goles:.2f}\n")

def guardar_tabla_posiciones(puntos_dict, carpeta):
    # Genera el reporte txt de la liga ordenado por puntos.
    ruta_archivo = os.path.join(carpeta, "tabla_posiciones.txt")
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("=== TABLA DE POSICIONES ===\n\n")
        f.write(f"{'Pos':<4} | {'Equipo':<25} | {'Puntos'}\n")
        f.write("-" * 40 + "\n")
        
        tabla_ordenada = sorted(puntos_dict.items(), key=lambda x: x[1], reverse=True)
        for i, (equipo, puntos) in enumerate(tabla_ordenada, start=1):
            f.write(f"{i:<4} | {equipo:<25} | {puntos}\n")

# Bloque de ejecución principal
if __name__ == "__main__": # Evita que el código se corra al ser importado
    # Definimos la carpeta de destino
    carpeta_resultados = "../resultados"
    
    # Por seguridad en entornos locales/colab, si por alguna razón la carpeta 
    # no existiera, esto la crea automáticamente sin romper el código.
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)
    
    # Recibimos todos los datos calculados
    victorias_dict, prom_goles, tabla_puntos = analizar_partidos()

    if victorias_dict is not None:
        # Guardamos cada reporte en su respectivo archivo
        guardar_ranking(victorias_dict, carpeta_resultados)
        guardar_estadisticas(prom_goles, carpeta_resultados)
        guardar_tabla_posiciones(tabla_puntos, carpeta_resultados)
        
        # Un pequeño aviso en consola para que el usuario sepa que todo salió bien
        print("¡Proceso completado con éxito!")
        print(f"Los archivos se han guardado correctamente en la carpeta '{carpeta_resultados}/'.")
