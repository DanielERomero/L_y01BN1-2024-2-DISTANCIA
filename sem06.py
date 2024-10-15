import streamlit as st

#titulo de la aplicacion
st.title("Ejercicios con bucles basicos en python")

#Ejercicio 1: Imprimir 10 veces 'hola mundo'
st.subheader("Ejercicio 1 Imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10): #range genera una secuencia de 0 al 9, for hace bucle
        st.write("Hola Mundo")

#Ejercicio 2: imprimir los primeros 10 numeros
st.subheader("ejercicio 2: imprimir los primeros 10 números")
if st.button("ejecutar Ejercicio 2"):
    for i in range(1, 11):
        st.write(i)
#Ejercicio: 3 Tabla de multiplicar
st.subheader("Ejercicio 3: Imprimir la tabla de multiplicar del numero ingresado")
num = st.number_input("Ingrese un número para ver su tabla de multiplicar del 1 al 12", min_value=1)
if st.button("Ejecutar Ejercicio 3"):
    for i in range(1, 13):
        st.write(f"{num} x {i} = {num * i}")