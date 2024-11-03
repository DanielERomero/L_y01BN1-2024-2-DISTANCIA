import streamlit as st

# Función para calcular los pagos mensuales y el total después de 20 meses
def calcular_pagos_mensuales_y_total(meses=20, pago_inicial=10):
    pagos = []  # Lista para almacenar los pagos mensuales
    pago_mensual = pago_inicial

    for mes in range(1, meses + 1):
        pagos.append(pago_mensual)
        pago_mensual *= 2  # Duplica el pago para el siguiente mes

    # Calcular el total pagado en los 20 meses
    total_pagado = sum(pagos)
    return pagos, total_pagado

# Título en la interfaz de Streamlit
st.title("Cálculo de Pagos Mensuales y Total después de 20 meses")

# Ejecutar el cálculo y mostrar los resultados cuando se presione el botón
if st.button("Calcular Pagos"):
    pagos, total_pagado = calcular_pagos_mensuales_y_total()
    st.write("Pagos mensuales:")
    for mes, pago in enumerate(pagos, start=1):
        st.write(f"Mes {mes}: S/{pago}")

    st.write("Total pagado después de 20 meses: S/", total_pagado)
#Ejecutar a funcion
if __name__ == "__main__":
    calcular_pagos_mensuales_y_total()