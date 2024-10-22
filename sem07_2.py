import streamlit as st

#función principal para verificar automoviles
def verificar_automoviles():
    st.title("Centro de Verificación de Automoviles")

    #lista para almacenar los puntos contaminantes
    if 'puntos_contaminantes' not is st.session_state:
        st.session_state.puntos_contaminantes = []

    #Input para los puntos contaminantes del automovil
    puntos = st.number_input("Ingrese los puntos contaminantes del automovil", min_value=0.0, step=0.1)

    #Botón para registrar automovil
    if st.button("Registrar automovil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automovil registrado con {puntos} puntos contaminantes. ")

    #mostrar los datos registrados hasta el momento
    if len(st.session_state.puntos_contaminantes) > 0 and st.button("Calcular resultados"):
        promedio = sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        menos_contaminantes = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        #mostrar los resultados
        st.write(f"promedio de puntos contaminantes: {promedio: .2f}")
        st.write(f"El automovil que menos conataminó tiene {menos_contaminacion}")
        st.write(f"El automovil que más contaminó tiene {mas_contaminacion}")

    #Opcion para reiniciar los datos
    if st.button("Reiniciar datos"):
        st.session_state.puntos_contaminantes =[]
        st.success("Datos reiniciados correctamente")

    #Ejecutar a funcion
    if __name__ == "__main__"
        verificar_automoviles()        
