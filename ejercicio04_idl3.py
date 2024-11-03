#ejercicio4 crear un programa que pida al usuario una contraseña de forma repetitiva minetras no introduzca "asdasd"
import streamlit as st
# Definir la contraseña correcta
CONTRASEÑA_CORRECTA = "asdasd"

def verificar_contraseña(contraseña):
    if contraseña == CONTRASEÑA_CORRECTA:
        return True
    else:
        return False
st.title("Ingreso de Contraseña")

contraseña = st.text_input("Introduce la contraseña:", type="password")

if contraseña:
    if verificar_contraseña(contraseña):
        st.write("Bienvenido")
    else:
        st.write("Contraseña incorrecta. Inténtalo de nuevo.")
