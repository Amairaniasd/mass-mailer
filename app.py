import streamlit as st

st.set_page_config(
    page_title="Mass Mailer",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Mass Mailer")
st.caption("Envío masivo de correos personalizados")

st.divider()

st.info("Usa el menú de la izquierda para navegar entre las secciones del proyecto.")

st.markdown("""
### ¿Qué hace esta app?
1. 📂 **Carga** un archivo CSV con contactos (exportado de Apollo u otra fuente)
2. ✉️ **Genera** correos personalizados con plantillas aleatorizadas
3. 🚀 **Envía** los correos vía SMTP sin ser detectado como spam
""")
