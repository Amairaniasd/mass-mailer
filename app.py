import os

import pandas as pd
import streamlit as st

from mailer.loader import load_contacts, preview_contacts
from mailer.sender import send_batch
from mailer.templates import render_template

st.set_page_config(page_title="Mass Mailer", layout="centered")

st.markdown("""
    <style>
        h1 { color: #1a1a2e; font-family: Georgia, serif; border-bottom: 2px solid #1a1a2e; padding-bottom: 0.5rem; }
        h2 { color: #16213e; font-family: Georgia, serif; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 1.5rem; }
        .stButton > button { background-color: #1a1a2e; color: white; border-radius: 4px; padding: 0.5rem 2rem; font-weight: 600; border: none; width: 100%; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)


def get_setting(name, default=""):
    try:
        return st.secrets.get(name, os.getenv(name, default))
    except Exception:
        return os.getenv(name, default)


def get_sendgrid_config():
    api_key = get_setting("SENDGRID_API_KEY")
    from_email = get_setting("SENDGRID_FROM_EMAIL")
    from_name = get_setting("SENDGRID_FROM_NAME", "Amairani Rosales")
    reply_to_email = get_setting("REPLY_TO_EMAIL", from_email)

    if not api_key or not from_email:
        return None

    return {
        "api_key": api_key,
        "from_email": from_email,
        "from_name": from_name,
        "reply_to_email": reply_to_email,
    }


def render_configured_template(contact):
    sender_name = get_setting("SENDGRID_FROM_NAME", "Amairani Rosales")
    reply_email = get_setting("REPLY_TO_EMAIL", get_setting("SENDGRID_FROM_EMAIL"))
    return render_template(contact, sender_name=sender_name, reply_email=reply_email)


def has_contacts():
    return "contacts" in st.session_state and len(st.session_state["contacts"]) > 0


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
st.header("2. Configuracion de envio")
sendgrid_config = get_sendgrid_config()
if sendgrid_config:
    st.session_state["sendgrid"] = sendgrid_config
    st.success(f"Remitente configurado: {sendgrid_config['from_email']}")
else:
    st.session_state.pop("sendgrid", None)
    st.warning("Configura SENDGRID_API_KEY y SENDGRID_FROM_EMAIL en los secretos de Streamlit.")

status_cols = st.columns(2)
with status_cols[0]:
    st.metric("Contactos listos", len(st.session_state["contacts"]) if has_contacts() else 0)
with status_cols[1]:
    st.metric("Servicio de envio", "Listo" if "sendgrid" in st.session_state else "Pendiente")

st.divider()
st.header("3. Vista previa")
st.caption("Genera una muestra del correo antes de enviar.")
if st.button("Generar vista previa", disabled=not has_contacts()):
    sample = st.session_state["contacts"].iloc[0].to_dict()
    subj, body = render_configured_template(sample)
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

if has_contacts():
    max_to_send = st.number_input(
        "Cantidad de correos a enviar",
        min_value=1,
        max_value=len(st.session_state["contacts"]),
        value=len(st.session_state["contacts"]),
        step=1,
    )
else:
    max_to_send = 0

confirmed = st.checkbox("Confirmo que el remitente y la lista son correctos")
ready_to_send = has_contacts() and "sendgrid" in st.session_state and confirmed and not st.session_state["sending"]

if st.button("Iniciar envio", type="primary", disabled=not ready_to_send):
    if not has_contacts():
        st.warning("Carga un archivo CSV antes de continuar.")
    elif "sendgrid" not in st.session_state:
        st.warning("Configura SendGrid antes de continuar.")
    elif not confirmed:
        st.warning("Confirma los datos antes de iniciar el envio.")
    else:
        st.session_state["sending"] = True
        st.session_state["results"] = []
        contacts_to_send = st.session_state["contacts"].head(max_to_send)
        progress = st.progress(0, text="Iniciando envio...")
        results = send_batch(
            contacts_to_send,
            st.session_state["sendgrid"],
            render_configured_template,
            progress_callback=lambda p: progress.progress(p, text=f"Enviando... {int(p*100)}%"),
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
