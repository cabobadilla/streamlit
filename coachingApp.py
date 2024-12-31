import streamlit as st
import openai

# Configura tu clave de API de OpenAI Done
openai.api_key = "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"

# Función para generar un plan personalizado
def generar_plan_personalizado(coaching, areas):
    prompt = f"Soy un coach experto. Un usuario está interesado en el coaching de tipo '{coaching}' y desea desarrollar las siguientes áreas: {', '.join(areas)}. Diseña un plan de trabajo personalizado, práctico y detallado para alcanzar sus objetivos."
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return respuesta.choices[0].text.strip()
    except Exception as e:
        return f"Error al generar el plan: {e}"

# Interfaz de la aplicación
st.title("Aplicación de Coaching Personalizado")

# Paso 1: Seleccionar tipo de coaching
st.header("1. Selecciona el tipo de coaching que te interesa")
tipos_coaching = ["Coaching Personal", "Coaching Profesional", "Coaching de Salud", "Coaching Deportivo", "Coaching de Relaciones"]
coaching_seleccionado = st.selectbox("Elige un tipo de coaching:", tipos_coaching)

# Paso 2: Seleccionar áreas de interés
st.header("2. ¿Qué áreas te interesa desarrollar?")
areas_disponibles = {
    "Coaching Personal": ["Gestión del estrés", "Autoestima", "Toma de decisiones"],
    "Coaching Profesional": ["Liderazgo", "Gestión del tiempo", "Trabajo en equipo"],
    "Coaching de Salud": ["Hábitos alimenticios", "Ejercicio", "Salud mental"],
    "Coaching Deportivo": ["Resistencia", "Técnica", "Mentalidad ganadora"],
    "Coaching de Relaciones": ["Comunicación", "Resolución de conflictos", "Empatía"]
}

if coaching_seleccionado:
    areas_seleccionadas = st.multiselect(
        "Elige las áreas que deseas trabajar:",
        areas_disponibles[coaching_seleccionado]
    )

# Paso 3: Generar plan personalizado
if st.button("Generar Plan Personalizado"):
    if coaching_seleccionado and areas_seleccionadas:
        st.header("Plan Personalizado")
        plan = generar_plan_personalizado(coaching_seleccionado, areas_seleccionadas)
        st.write(plan)
    else:
        st.warning("Por favor, selecciona un tipo de coaching y al menos un área de interés.")

# Instrucciones para ejecutar la app
st.sidebar.title("Instrucciones")
st.sidebar.write("1. Asegúrate de tener Streamlit instalado: `pip install streamlit`.\n")
st.sidebar.write("2. Guarda este archivo como `app.py`.\n")
st.sidebar.write("3. Ejecuta el comando `streamlit run app.py` en tu terminal para iniciar la aplicación.")
ß