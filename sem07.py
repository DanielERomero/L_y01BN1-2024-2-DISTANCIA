import streamlit as st

def mostrar_menu():
    st.title("Ejemplo de Menú")
    st.write("Selecciona una opcion del menú")

    menu = ["archivo","Editar","Ver","Salir"]
    seleccion = ""

    
    seleccion = st.radio("Menú", menu)

    if seleccion == "Archivo":
        st.write("seleccionaste: archivo")
     elif seleccion == "Editar":
        st.write("Seleccionaste: Editar")
    elif seleccion == "Salir":
        st.write("¡Saliendo del menú")
            
if __name__ == "__main__":
    mostrar_menu()                    