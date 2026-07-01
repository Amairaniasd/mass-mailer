import streamlit as st
from mailer.loader import load_contacts, preview_contacts
from mailer.templates import render_template

st.set_page_config(
    page_title="Mass Mailer",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Mass Mailer")
st.caption("Envío masivo de correos personalizados")
st.divider()

# --- SECCIÓN 1: Cargar CSV ---
st.header("1. 📂 Cargar contactos")
uploaded = st.file_uploader("Sube tu CSV de Apollo", type=["csv", "xls", "xlsx"])

if uploaded:
    try:
        df = load_contacts(uploaded)
        st.success(f"{len(df)} contactos verificados cargados.")
        st.dataframe(preview_contacts(df))
        st.session_state["contacts"] = df
    except ValueError as e:
        st.error(str(e))

# --- SECCIÓN 2: Credenciales SMTP ---
st.divider()
st.header("2. ✉️ Configuración SMTP")

col1, col2 = st.columns(2)
with col1:
    smtp_host = st.text_input("Servidor SMTP", value="smtp.gmail.com")
    smtp_user = st.text_input("Correo remitente")
with col2:
    smtp_port = st.number_input("Puerto", value=587)
    smtp_pass = st.text_input("Contraseña / App Password", type="password")

if smtp_host and smtp_user and smtp_pass:
    st.session_state["smtp"] = {
        "host": smtp_host,
        "port": int(smtp_port),
        "user": smtp_user,
        "password": smtp_pass,
    }
    st.success("Credenciales guardadas.")

# --- SECCIÓN 3: Preview ---
st.divider()
st.header("3. 👁️ Vista previa de plantilla")

if st.button("Generar preview"):
    if "contacts" not in st.session_state:
        st.warning("Primero carga un CSV.")
    else:
        sample = st.session_state["contacts"].iloc[0].to_dict()
        subj, body = render_template(sample)
        st.text_input("Asunto", value=subj, disabled=True)
        st.text_area("Cuerpo", value=body, height=200, disabled=True)
