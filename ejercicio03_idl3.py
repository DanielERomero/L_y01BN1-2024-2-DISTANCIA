import streamlit as st

# Función para pedir números y calcular la suma y la media
def calcular_suma_y_media():
    numeros = []  # Lista para almacenar los números introducidos

    st.write("Introduce números uno a uno. Escribe '0' para terminar:")

    while True:
        numero = st.number_input("Introduce un número:", step=1.0, key=len(numeros))
        
        # Si el número es cero, terminamos el bucle
        if numero == 0:
            break
        else:
            numeros.append(numero)

    # Calcular la suma y la media
    suma = sum(numeros)
    media = suma / len(numeros) if numeros else 0

    return suma, media

# Título en la interfaz de Streamlit
st.title("Cálculo de Suma y Media de Números")

# Ejecutar la función y mostrar los resultados cuando se presione el botón
if st.button("Calcular"):
    suma, media = calcular_suma_y_media()
    st.write("Suma de los números introducidos:", suma)
    st.write("Media de los números introducidos:", media)

