import streamlit as st
import math

def main():
    st.set_page_config(page_title="Calculadora estilo Mac", layout="centered")
    
    # Estilos CSS para diseño en blanco y negro
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Courier New', Courier, monospace;
        }
        .calculator {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            max-width: 300px;
            margin: 0 auto;
        }
        .calculator button {
            background-color: white;
            color: black;
            border: none;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .calculator button:hover {
            background-color: #e6e6e6;
        }
        .display {
            grid-column: span 4;
            background-color: white;
            color: black;
            font-size: 24px;
            padding: 15px;
            text-align: right;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='calculator'>", unsafe_allow_html=True)

    # Display de la calculadora
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""

    display_text = st.session_state.input_text

    st.markdown(f"<div class='display'>{display_text}</div>", unsafe_allow_html=True)

    # Botones de la calculadora
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+",
    ]

    col1, col2, col3, col4 = st.columns(4)

    def on_click(label):
        if label == "=":
            try:
                # Evalúa la expresión
                st.session_state.input_text = str(eval(st.session_state.input_text))
            except Exception:
                st.session_state.input_text = "Error"
        elif label == "C":
            # Reinicia la entrada
            st.session_state.input_text = ""
        else:
            # Actualiza la entrada
            st.session_state.input_text += label

    for i, label in enumerate(buttons):
        with [col1, col2, col3, col4][i % 4]:
            st.button(label, key=label, on_click=lambda l=label: on_click(l))

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
