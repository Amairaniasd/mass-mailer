# 📧 Mass Mailer

Aplicación web construida con Python + Streamlit para el envío masivo de correos personalizados, diseñada para evitar detección como spam mediante aleatorización de plantillas.

## Tecnologías
- Python 3.10+
- Streamlit
- Pandas
- smtplib (librería estándar de Python)

## Instalación

```bash
git clone https://github.com/Amairaniasd/mass-mailer.git
cd mass-mailer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Cronograma

| Semana | Entregable | Estado |
|--------|------------|--------|
| 1 | Configuración del entorno y estructura base | ✅  |
| 2 | Carga y validación de CSV con Pandas | ✅  |
| 3 | Motor de aleatorización de plantillas | ✅  |
| 4 | Integración UI de credenciales SMTP |   |
| 5 | Barra de progreso y session_state |   |
| 6 | Pruebas, manejo de errores y deploy |   |
| 7 | Documentación técnica y refinamiento UI/UX |  |
