#ejercico 3: Algoritmo que pida numeros hasta que se introduzca un cero, imprimir la suma y la media de los numero introducido
import streamlit as st

# Función para pedir números y calcular la suma y la media
def calcular_suma_y_media():
    numeros = []  
    st.write("Introduce números uno a uno. Escribe '0' para terminar:")
    while True:
        numero = st.number_input("Introduce un número:", step=1.0, key=len(numeros))
        
        if numero == 0:
            break
        else:
            numeros.append(numero)
    suma = sum(numeros)
    media = suma / len(numeros) if numeros else 0

    return suma, media

st.title("Cálculo de Suma y Media de Números")

if st.button("Calcular"):
    suma, media = calcular_suma_y_media()
    st.write("Suma de los números introducidos:", suma)
    st.write("Media de los números introducidos:", media)
#Ejecutar a funcion
if __name__ == "__main__":
    calcular_suma_y_media()
