import streamlit as st

st.title("Ejercicio IDL3")

#Ejercicio 1: calcular y mostrar la suma de los número pares comprendidos entre 20 y 400
st.subheader("Ejercicio1: Suma de numero pares")
if st.button("Ejecutar ejercicio 1: "):
    suma_pares = sum(num for num in range (2, 401) if num % 2 == 0)
    #mostrar el resultado:
    st.write(f"La suma de los numeros pares entre 20 y 400 es: {suma_pares}")

#Ejercicio 2: Dado las notas de un estudiante calcular cuantas notas tienes desaprobados y cuantos aprobados
import streamlit as st

# Función para contar las notas aprobadas
def contar_aprobadas(notas):
    return len([nota for nota in notas if nota >= 11])

# Función para contar las notas desaprobadas
def contar_desaprobadas(notas):
    return len([nota for nota in notas if nota < 11])

# Función para calcular el promedio de las notas
def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

# Función principal para procesar las notas
def procesar_notas(notas):
    aprobadas = contar_aprobadas(notas)
    desaprobadas = contar_desaprobadas(notas)
    promedio = calcular_promedio(notas)
    return aprobadas, desaprobadas, promedio

# Título de la aplicación en Streamlit
st.title("Análisis de Notas del Estudiante")

# Entrada de las notas como lista
notas_input = st.text_input("Ingresa las notas separadas por comas:")

# Procesar las notas cuando se ingresa una entrada
if notas_input:
    # Convertir la entrada en una lista de números
    notas = list(map(float, notas_input.split(',')))

    # Llamar a la función principal para obtener resultados
    aprobadas, desaprobadas, promedio = procesar_notas(notas)

    # Mostrar los resultados
    st.write("Cantidad de notas aprobadas:", aprobadas)
    st.write("Cantidad de notas desaprobadas:", desaprobadas)
    st.write("Promedio de todas las notas:", promedio)

#ejercico 3: Algoritmo que pida numeros hasta que se introduzca un cero, imprimir la suma y la media de los numero introducido
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
#Ejecutar a funcion
if __name__ == "__main__":
    calcular_suma_y_media()


