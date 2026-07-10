# Mass Mailer

Aplicacion web construida con Python + Streamlit para el envio masivo de correos personalizados con contactos verificados de Apollo y plantillas aleatorias.

## Tecnologias

- Python 3.10+
- Streamlit
- Pandas
- SendGrid

## Instalacion

```bash
git clone https://github.com/Amairaniasd/mass-mailer.git
cd mass-mailer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Configuracion de SendGrid

La API Key no debe escribirse en el codigo. Para ejecucion local, crea `.streamlit/secrets.toml` con:

```toml
SENDGRID_API_KEY = "tu_api_key_de_sendgrid"
SENDGRID_FROM_EMAIL = "informaitesi@gmail.com"
SENDGRID_FROM_NAME = "Amairani Rosales"
```

En Streamlit Cloud, agrega esos mismos valores en `Settings > Secrets`.

Antes de enviar correos reales:

- Crear la cuenta de SendGrid con `informaitesi@gmail.com`.
- Verificar `informaitesi@gmail.com` como Single Sender.
- Generar una API Key nueva.
- Regenerar o borrar cualquier API Key anterior que se haya compartido o subido por error.

## Cronograma

| Semana | Entregable | Estado |
|--------|------------|--------|
| 1 | Configuracion del entorno y estructura base | Completado |
| 2 | Carga y validacion de CSV con Pandas | Completado |
| 3 | Motor de aleatorizacion de plantillas | Completado |
| 4 | Configuracion de envio con SendGrid | Completado |
| 5 | Barra de progreso y session_state | Completado |
| 6 | Pruebas, manejo de errores y deploy | Completado |
| 7 | Documentacion tecnica y refinamiento UI/UX | Pendiente |
