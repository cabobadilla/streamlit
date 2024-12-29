import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cocinando con Pao", page_icon="🍲", layout="centered")

# Estilo con imagen de fondo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://via.placeholder.com/1080x1920.png?text=Imagen+de+Cocina');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    h1 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    label, .stTextInput {
        color: white;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    }
    .stButton > button {
        background-color: #ff4d4d;
        border: none;
        color: white;
        padding: 10px;
        font-size: 1em;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #ff0000;
    }
    .output {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
        padding: 10px;
        margin-top: 10px;
        font-size: 1.2em;
        color: #333;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("Cocinando con Pao")

# Formulario para ingresar la cantidad de harina
gramos = st.number_input("Introduce la cantidad de harina en gramos:", min_value=0.0, step=1.0)

# Botón para calcular
if st.button("Convertir"):
    cucharadas = gramos / 8.0  # Aproximadamente 8 gramos por cucharada
    tazas = gramos / 120.0  # Aproximadamente 120 gramos por taza
    
    # Mostrar los resultados
    st.markdown(
        f"""
        <div class='output'>
            <strong>Equivalencias:</strong><br>
            {gramos} gramos son aproximadamente:<br>
            {cucharadas:.2f} cucharadas<br>
            {tazas:.2f} tazas
        </div>
        """,
        unsafe_allow_html=True
    )
