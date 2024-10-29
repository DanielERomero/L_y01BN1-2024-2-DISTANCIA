import streamlit as st

def validate_data(marca, modelo, kilometraje):
    """Valida los datos ingresados para el automovil. """
    if not marca or not modelo:
        return "La marca y el modelo no deben estar vacíos."
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            return "El kilometraje no puede ser menor que 0"
    except valueError:
        return "El kilometraje debe ser un número válido"
    return None

def main():
    st.title("Registro de Automóvil")
    st.write("Ingrese los datos del automovil a continuacion: ")

    #Registro por el usuario
    marca = st.text_input("Marca del automovil")
    modelo = st.text_input("Modelo del automovil")
    kilometraje = st.text_input("kilometraje del automovil")

    if st.button("registrar"):
        #validacion de los datos
        error = validate_data(marca, modelo, kilometraje)
        if error:
            st.error(error)
        else:
            st.success("Automovil registrado exitosamente.")
            st.write("**Marca:**",marca)
            st.write("**Modelo:**",modelo)
            st.write("**kilometrage**",kilometraje)

if __name__ == "__main__":
    main()     