# Catálogo temporal de materias (luego lo cargas de Mongo/CSV)
MATERIAS = {
    "MATE1101": {"nombre": "Cálculo I", "creditos": 4},
    "ISIS2603": {"nombre": "Des. Web", "creditos": 3},
    "FISI1201": {"nombre": "Física I", "creditos": 4},
}

def recomendar_dummy(codigo, materias):
    return {
        "cluster": "Cluster 2 (placeholder)",
        "recomendaciones": [
            {"materia": "ISIS2603", "razón": "Similitud por estilo académico"},
            {"materia": "MATE1202", "razón": "Estudiante en cluster 2 suele tomarla"}
        ],
        "explicacion": "Este es un ejemplo temporal. El modelo real irá aquí."
    }
