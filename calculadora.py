import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora", page_icon="⚙", layout="centered")

# Estilo para aplicar el color rojo
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6e6;
    }
    h1 {
        color: #b30000;
    }
    .stButton > button {
        background-color: #ff4d4d;
        color: white;
        border: none;
    }
    .stButton > button:hover {
        background-color: #ff0000;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("Calculadora Roja")

# Entrada de números
st.write("Ingresa dos números para realizar una operación:")
num1 = st.number_input("Número 1", value=0.0, step=0.1)
num2 = st.number_input("Número 2", value=0.0, step=0.1)

# Selección de operación
operation = st.selectbox("Selecciona una operación:", ["Suma", "Resta", "Multiplicación", "División"])

# Botón para calcular
if st.button("Calcular"):
    if operation == "Suma":
        result = num1 + num2
        st.success(f"El resultado de la suma es: {result}")
    elif operation == "Resta":
        result = num1 - num2
        st.success(f"El resultado de la resta es: {result}")
    elif operation == "Multiplicación":
        result = num1 * num2
        st.success(f"El resultado de la multiplicación es: {result}")
    elif operation == "División":
        if num2 != 0:
            result = num1 / num2
            st.success(f"El resultado de la división es: {result}")
        else:
            st.error("Error: No se puede dividir entre cero.")
