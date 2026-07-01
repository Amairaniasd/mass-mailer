import streamlit as st
import pandas as pd
from mailer.loader import load_contacts, preview_contacts
from mailer.templates import render_template
from mailer.sender import send_batch

st.set_page_config(page_title="Mass Mailer", layout="centered")

st.markdown("""
    <style>
        h1 { color: #1a1a2e; font-family: Georgia, serif; border-bottom: 2px solid #1a1a2e; padding-bottom: 0.5rem; }
        h2 { color: #16213e; font-family: Georgia, serif; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 1.5rem; }
        .stButton > button { background-color: #1a1a2e; color: white; border-radius: 4px; padding: 0.5rem 2rem; font-weight: 600; border: none; width: 100%; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

st.title("Mass Mailer")
st.caption("Sistema de envio masivo de correos personalizados")
st.divider()

st.header("1. Cargar contactos")
uploaded = st.file_uploader("Selecciona un archivo CSV exportado de Apollo", type=["csv", "xls", "xlsx"])
if uploaded:
    try:
        df = load_contacts(uploaded)
        st.success(f"{len(df)} contactos verificados encontrados.")
        st.dataframe(preview_contacts(df), use_container_width=True)
        st.session_state["contacts"] = df
    except ValueError as e:
        st.error(str(e))

st.divider()
st.header("2. Configuracion SMTP")
st.caption("Para Gmail usa un App Password, no tu contrasena normal.")
col1, col2 = st.columns(2)
with col1:
    smtp_host = st.text_input("Servidor SMTP", value="smtp.gmail.com")
    smtp_user = st.text_input("Correo remitente")
with col2:
    smtp_port = st.number_input("Puerto", value=587)
    smtp_pass = st.text_input("App Password", type="password")
if smtp_host and smtp_user and smtp_pass:
    st.session_state["smtp"] = {"host": smtp_host, "port": int(smtp_port), "user": smtp_user, "password": smtp_pass}
    st.success("Credenciales configuradas correctamente.")

st.divider()
st.header("3. Vista previa")
st.caption("Genera una muestra del correo antes de enviar.")
if st.button("Generar vista previa"):
    if "contacts" not in st.session_state:
        st.warning("Carga un archivo CSV antes de continuar.")
    else:
        sample = st.session_state["contacts"].iloc[0].to_dict()
        subj, body = render_template(sample)
        st.session_state["preview_subject"] = subj
        st.session_state["preview_body"] = body
if "preview_subject" in st.session_state:
    st.text_input("Asunto", value=st.session_state["preview_subject"], disabled=True)
    st.text_area("Cuerpo", value=st.session_state["preview_body"], height=220, disabled=True)

st.divider()
st.header("4. Envio de correos")
st.caption("No cierres esta ventana durante el proceso de envio.")
if "sending" not in st.session_state:
    st.session_state["sending"] = False
if "results" not in st.session_state:
    st.session_state["results"] = []

if st.button("Iniciar envio", type="primary", disabled=st.session_state["sending"]):
    if "contacts" not in st.session_state:
        st.warning("Carga un archivo CSV antes de continuar.")
    elif "smtp" not in st.session_state:
        st.warning("Configura las credenciales SMTP antes de continuar.")
    else:
        st.session_state["sending"] = True
        st.session_state["results"] = []
        progress = st.progress(0, text="Iniciando envio...")
        results = send_batch(
            st.session_state["contacts"],
            st.session_state["smtp"],
            render_template,
            progress_callback=lambda p: progress.progress(p, text=f"Enviando... {int(p*100)}%")
        )
        st.session_state["results"] = results
        st.session_state["sending"] = False
        enviados = sum(1 for r in results if r["Estado"] == "Enviado")
        st.success(f"Proceso completado. {enviados} de {len(results)} correos enviados.")

if st.session_state["results"]:
    st.divider()
    st.header("5. Resultados")
    results_df = pd.DataFrame(st.session_state["results"])
    st.dataframe(results_df, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Enviados", sum(1 for r in st.session_state["results"] if r["Estado"] == "Enviado"))
    with col2:
        st.metric("Errores", sum(1 for r in st.session_state["results"] if "Error" in r["Estado"]))
