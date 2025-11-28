import pandas as pd
import streamlit as st
from models import MATERIAS, recomendar_dummy

codigo_est = st.text_input("Código del estudiante")

materia_input = st.text_input("Agregar materia por código")

if st.button("Agregar materia"):
    if materia_input not in st.session_state.materias_seleccionadas:
        st.session_state.materias_seleccionadas.append(materia_input)


if "materias_seleccionadas" not in st.session_state:
    st.session_state.materias_seleccionadas = []

df = pd.DataFrame([
    {
        "codigo": m,
        "materia": MATERIAS[m]["nombre"],
        "creditos": MATERIAS[m]["creditos"]
    }
    for m in st.session_state.materias_seleccionadas
])

st.dataframe(df)

total_creditos = df.get("creditos", None)
if total_creditos is None:
    total_creditos = 0
else:
    total_creditos = total_creditos.sum()
    
st.markdown(f"### Total créditos: **{total_creditos}**")

if st.button("Calcular recomendaciones"):
    resultado = recomendar_dummy(
        codigo_est,
        st.session_state.materias_seleccionadas
    )
    st.success("Recomendaciones generadas")
    st.write(resultado)

