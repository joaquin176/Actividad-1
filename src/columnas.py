# 1) Estructura de columnas
COLUMNAS = {
    "PONDERA":    {"tipo": "int",    "completitud": 98},
    "ESTADO":     {"tipo": "int",    "completitud": 95},
    "CAT_OCUP":   {"tipo": "int",    "completitud": 80},
    "EDAD":       {"tipo": "int",    "completitud": 99},
    "REGION":     {"tipo": "int",    "completitud": 100},
    "AGLOMERADO": {"tipo": "int",    "completitud": 100},
    "MAS_500":    {"tipo": "string", "completitud": 100},
    "ANO4":       {"tipo": "int",    "completitud": 100},
    "TRIMESTRE":  {"tipo": "int",    "completitud": 100},
    "ITF":        {"tipo": "int",    "completitud": 72},
    "GDECCFR":    {"tipo": "int",    "completitud": 68},
}

# 2) Estructura de roles
ROLES = {
    "docente": {
        "columnas": ["EDAD", "ESTADO", "REGION", "TRIMESTRE", "ANO4"],
        "orden_por": "nombre",
        "orden_forma": "A",
    },
    "investigador": {
        "columnas": ["ITF", "GDECCFR", "CAT_OCUP", "ESTADO", "EDAD", "REGION"],
        "orden_por": "completitud",
        "orden_forma": "B",
        "completitud_minima": 70,   
    },
    "analista": {
        "columnas": list(COLUMNAS.keys()),
        "orden_por": "completitud",
        "orden_forma": "B",
        "completitud_minima": 90,   
    },
}

def informar_columnas(rol=None):
    """
    Genera e imprime el reporte de columnas filtradas según el rol.
    Utiliza filter() para excluir columnas por debajo del umbral, 
    y map() para formatear las líneas del reporte final.
    """
    
    # CASO 1: Informe general por defecto (sin rol)
    if rol is None:
        print("\n--- Informe general (todas las columnas) ---")
        
        columnas_ordenadas = sorted(
            COLUMNAS.keys(),
            key=lambda c: COLUMNAS[c]["completitud"],
            reverse=True
        )
        
        lineas_reporte = list(map(
            lambda c: f"- {c:<12} | Tipo: {COLUMNAS[c]['tipo']:<6} | Completitud: {COLUMNAS[c]['completitud']}%", 
            columnas_ordenadas
        ))
        print("\n".join(lineas_reporte))
        return

    # CASO 2: Informe específico por rol
    if rol not in ROLES:
        print(f"\nError: El rol '{rol}' no existe. Opciones válidas: {list(ROLES.keys())}")
        return

    config = ROLES[rol]
    columnas_filtradas = config["columnas"]

    # Deja pasar solo las columnas que superan el mínimo
    if "completitud_minima" in config:
        minimo = config["completitud_minima"]
        columnas_filtradas = list(filter(
            lambda c: COLUMNAS[c]["completitud"] >= minimo, 
            columnas_filtradas
        ))

    # Configuramos el sentido del orden (Ascendente o Descendente)
    if config["orden_forma"] == "B":
        es_descendente = True
    else:
        es_descendente = False

    if config["orden_por"] == "nombre":
        columnas_ordenadas = sorted(columnas_filtradas, reverse=es_descendente)
    else: 
        columnas_ordenadas = sorted(
            columnas_filtradas, 
            key=lambda c: COLUMNAS[c]["completitud"], 
            reverse=es_descendente
        )

    # Impresión final de los resultados
    print(f"\n--- Informe para el rol: {rol.capitalize()} ---")
    
    if not columnas_ordenadas:
        print("Ninguna columna cumple con los requisitos de este rol.")
    else:
        # APLICACIÓN DE MAP
        lineas_reporte = list(map(
            lambda c: f"- {c:<12} | Tipo: {COLUMNAS[c]['tipo']:<6} | Completitud: {COLUMNAS[c]['completitud']}%", 
            columnas_ordenadas
        ))
        print("\n".join(lineas_reporte))


if __name__ == "__main__":
    informar_columnas()              
    informar_columnas("docente")
    informar_columnas("investigador")
    informar_columnas("analista")