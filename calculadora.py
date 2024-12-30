import streamlit as st
import math

def main():
    st.set_page_config(page_title="Calculadora estilo Mac", layout="centered")
    
    # Estilos CSS para diseño inspirado en la calculadora de Mac
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .calculator {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            max-width: 350px;
            margin: 0 auto;
        }
        .calculator button {
            background-color: #d3d3d3;
            color: black;
            border: none;
            font-size: 20px;
            font-weight: bold;
            padding: 20px;
            cursor: pointer;
            border-radius: 10px;
        }
        .calculator button.operation {
            background-color: #f6a600;
            color: white;
        }
        .calculator button.operation:hover {
            background-color: #e69500;
        }
        .calculator button.clear {
            background-color: #a5a5a5;
        }
        .calculator button.clear:hover {
            background-color: #8e8e8e;
        }
        .display {
            grid-column: span 4;
            background-color: black;
            color: white;
            font-size: 36px;
            padding: 20px;
            text-align: right;
            border: 1px solid #d3d3d3;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='calculator'>", unsafe_allow_html=True)

    # Display de la calculadora
    if 'input_text' not in st.session_state:
        st.session_state.input_text = "0"

    display_text = st.session_state.input_text

    st.markdown(f"<div class='display'>{display_text}</div>", unsafe_allow_html=True)

    # Botones de la calculadora
    buttons = [
        {"label": "AC", "class": "clear"}, {"label": "+/-", "class": "clear"}, {"label": "%", "class": "clear"}, {"label": "/", "class": "operation"},
        {"label": "7", "class": ""}, {"label": "8", "class": ""}, {"label": "9", "class": ""}, {"label": "*", "class": "operation"},
        {"label": "4", "class": ""}, {"label": "5", "class": ""}, {"label": "6", "class": ""}, {"label": "-", "class": "operation"},
        {"label": "1", "class": ""}, {"label": "2", "class": ""}, {"label": "3", "class": ""}, {"label": "+", "class": "operation"},
        {"label": "0", "class": "", "span": 2}, {"label": ".", "class": ""}, {"label": "=", "class": "operation"}
    ]

    col1, col2, col3, col4 = st.columns(4)

    def on_click(label):
        if label == "=":
            try:
                # Evalúa la expresión
                st.session_state.input_text = str(eval(st.session_state.input_text))
            except Exception:
                st.session_state.input_text = "Error"
        elif label == "AC":
            # Reinicia la entrada
            st.session_state.input_text = "0"
        elif label == "+/-":
            # Cambia el signo del número
            if st.session_state.input_text.startswith("-"):
                st.session_state.input_text = st.session_state.input_text[1:]
            else:
                st.session_state.input_text = "-" + st.session_state.input_text
        elif label == "%":
            # Convierte a porcentaje
            try:
                st.session_state.input_text = str(float(st.session_state.input_text) / 100)
            except Exception:
                st.session_state.input_text = "Error"
        else:
            # Actualiza la entrada
            if st.session_state.input_text == "0":
                st.session_state.input_text = label
            else:
                st.session_state.input_text += label

    for button in buttons:
        button_label = button["label"]
        button_class = button.get("class", "")
        span = button.get("span", 1)

        if span == 2:
            with col1:
                st.markdown(
                    f"<button class='{button_class}' style='grid-column: span 2;' onclick="" on_click=lambda l=button_label: on_click(l)"> {button_label}</button>",
                    unsafe_allow_html=True
                )
        else:
            with [col1, col2, col3, col4][buttons.index(button) % 4]:
                st.button(button_label, key=button_label, on_click=lambda l=button_label: on_click(l))

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
