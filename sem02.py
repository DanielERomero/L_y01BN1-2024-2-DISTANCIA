import streamlit as st

#inicialización de variables 
usuarios = []

#Función para agragar un usuario
def agregar_usuario(nombre):
    usuarios.append(nombre)
    st.success(f"usuario {nombre} agregado.")

#Función para mostrar usuarios
def mostrar_usuarios():
    if usuarios:
        st.write("Lista de usuarios:")
        for usuario in usuario:
            st.white(f"-{usuario}")
    else:
        st.warning("No hay usuarios registrados.")

#Menú Principal
st.title("Gestión de Usuarios")

opcion = st.selectbox("Selecciona una opcion", ["Agregar Usuario","Mostrar Usuario"])

if opcion == "Agregar Usuario":
    nombre = st.text_input("Nombre del Usuario")
    if st.button("Agregar"):
        if nombre:
            agregar_usuario(nombre)
        else:
            st.error("El nombre no puede estar vacío")

elif opcion == "Mostrar Usuarios"
     mostrar_usuarios()          

