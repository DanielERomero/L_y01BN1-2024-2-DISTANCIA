import streamlit as st

st.title("Ejercicio IDL3")

#Ejercicio 1: calcular y mostrar la suma de los número pares comprendidos entre 20 y 400
st.subheader("Ejercicio1: Suma de numero pares")
if st.button("Ejecutar ejercicio 1: "):
    suma_pares = sum(num for num in range (2, 401) if num % 2 == 0)
    #mostrar el resultado:
    st.write(f"La suma de los numeros pares entre 20 y 400 es: {suma_pares}")


     


