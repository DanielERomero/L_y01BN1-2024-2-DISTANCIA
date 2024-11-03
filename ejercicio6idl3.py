import streamlit as st

# Función para encontrar múltiplos de X entre 0 y 100
def calcular_multiplos(x):
    multiplos = []  # Lista para almacenar los múltiplos de X

    # Iterar sobre el rango de 0 a 100 y agregar múltiplos a la lista
    for i in range(0, 101):
        if i % x == 0:
            multiplos.append(i)

    # Retornar la cantidad de datos y la sumatoria
    cantidad_datos = len(multiplos)
    sumatoria_datos = sum(multiplos)
    return cantidad_datos, sumatoria_datos, multiplos

# Título de la aplicación en Streamlit
st.title("Cálculo de Múltiplos de X entre 0 y 100")

# Entrada para el valor de X
x = st.number_input("Introduce el valor de X:", min_value=1, step=1)

# Ejecutar el cálculo y mostrar los resultados cuando se presione el botón
if st.button("Calcular Múltiplos"):
    cantidad, suma, multiplos = calcular_multiplos(x)
    
    # Mostrar resultados
    st.write(f"Múltiplos de {x} entre 0 y 100: {multiplos}")
    st.write(f"Cantidad de múltiplos encontrados: {cantidad}")
    st.write(f"Sumatoria de los múltiplos: {suma}")
