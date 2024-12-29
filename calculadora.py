import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Avanzada", page_icon="⚙", layout="centered")

# Estilo para aplicar los colores rojo y azul
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    h1 {
        color: #004080;
    }
    .screen {
        background-color: #ffffff;
        border: 2px solid #004080;
        border-radius: 5px;
        padding: 10px;
        text-align: right;
        font-size: 2em;
        color: #004080;
    }
    .button {
        background-color: #ff4d4d;
        border: none;
        border-radius: 5px;
        color: white;
        font-size: 1.5em;
        padding: 10px;
        margin: 5px;
        width: 60px;
    }
    .button:hover {
        background-color: #ff0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("Calculadora Roja y Azul")

# Variables para la calculadora
if 'input_value' not in st.session_state:
    st.session_state.input_value = ""

# Función para manejar la entrada
def button_click(value):
    if value == "C":
        st.session_state.input_value = ""
    elif value == "=":
        try:
            st.session_state.input_value = str(eval(st.session_state.input_value))
        except Exception:
            st.session_state.input_value = "Error"
    else:
        st.session_state.input_value += value

# Pantalla
st.markdown(f"<div class='screen'>{st.session_state.input_value}</div>", unsafe_allow_html=True)

# Botones
cols = st.columns(4)
buttons = [
    ("7", cols[0]), ("8", cols[1]), ("9", cols[2]), ("/", cols[3]),
    ("4", cols[0]), ("5", cols[1]), ("6", cols[2]), ("*", cols[3]),
    ("1", cols[0]), ("2", cols[1]), ("3", cols[2]), ("-", cols[3]),
    ("0", cols[0]), ("C", cols[1]), ("=", cols[2]), ("+", cols[3])
]

for (label, col) in buttons:
    with col:
        if st.button(label, key=label, help=f"Botón {label}", kwargs={"className": "button"}):
            button_click(label)
