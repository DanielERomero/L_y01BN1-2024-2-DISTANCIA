#ejercico 3: Algoritmo que pida numeros hasta que se introduzca un cero, imprimir la suma y la media de los numero introducido
import streamlit as st

# Título de la aplicación
st.title("Suma y Media de Números")

# Inicializar la lista para almacenar los números
numeros = []

# Entrada de números
st.write("Introduce números (introduce 0 para finalizar):")

# Ciclo para solicitar números hasta que se introduzca 0
while True:
    numero = st.number_input("Número:", step=1, format="%d")
    
    if numero == 0:
        break  # Salir del bucle si se introduce 0
    else:
        numeros.append(numero)  # Agregar el número a la lista

# Calcular suma y media
if numeros:
    suma = sum(numeros)
    media = suma / len(numeros)
    
    # Mostrar resultados
    st.write(f"Suma de los números introducidos: {suma}")
    st.write(f"Media de los números introducidos: {media:.2f}")
else:
    st.write("No se han introducido números.")

#Ejecutar a funcion
if __name__ == "__main__":
    calcular_suma_y_media()
