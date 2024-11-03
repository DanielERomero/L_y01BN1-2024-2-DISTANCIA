import streamlit as st
import math

# Procedimiento para calcular el perímetro de una circunferencia
def calcular_perimetro(radio):
    return 2 * math.pi * radio

# Procedimiento para calcular el área de una circunferencia
def calcular_area(radio):
    return math.pi * (radio ** 2)

# Título de la aplicación en Streamlit
st.title("Cálculo del Área y Perímetro de una Circunferencia")

# Entrada para el radio de la circunferencia
radio = st.number_input("Introduce el radio de la circunferencia:", min_value=0.0, step=0.1)

# Ejecutar los cálculos y mostrar los resultados cuando se presione el botón
if st.button("Calcular"):
    perimetro = calcular_perimetro(radio)
    area = calcular_area(radio)
    
    # Mostrar resultados
    st.write("Perímetro de la circunferencia: {:.2f}".format(perimetro))
    st.write("Área de la circunferencia: {:.2f}".format(area))

