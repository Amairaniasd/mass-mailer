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
REPLY_TO_EMAIL = "informaitesi@gmail.com"
```

En Streamlit Cloud, agrega esos mismos valores en `Settings > Secrets`.

Antes de enviar correos reales:

- Crear la cuenta de SendGrid con `informaitesi@gmail.com`.
- Verificar `informaitesi@gmail.com` como Single Sender.
- Generar una API Key nueva.
- Regenerar o borrar cualquier API Key anterior que se haya compartido o subido por error.

Para mejorar la entregabilidad, lo ideal es autenticar un dominio propio en SendGrid. La verificacion de Single Sender sirve para pruebas, pero la autenticacion de dominio con SPF, DKIM y DMARC da mas confianza a Gmail y Outlook.

## Flujo de uso

1. Cargar el archivo CSV, XLS o XLSX exportado desde Apollo.
2. Revisar que la app haya conservado solo contactos con `Email Status = verified`.
3. Confirmar que SendGrid este configurado con el remitente correcto.
4. Generar una vista previa del asunto y cuerpo.
5. Elegir la cantidad de correos a enviar.
6. Confirmar la lista y ejecutar el envio.
7. Revisar la tabla de resultados.

## Validaciones incluidas

- Columnas requeridas: `First Name`, `Last Name`, `Email`, `Email Status`.
- Filtrado automatico de contactos no verificados.
- Eliminacion de filas sin correo.
- Validacion basica de correos con `@`.
- Retraso aleatorio de 3 a 8 segundos entre envios.
- Resultados separados entre enviados y errores.

## Cronograma

| Semana | Entregable | Estado |
|--------|------------|--------|
| 1 | Configuracion del entorno y estructura base | Completado |
| 2 | Carga y validacion de CSV con Pandas | Completado |
| 3 | Motor de aleatorizacion de plantillas | Completado |
| 4 | Configuracion de envio con SendGrid | Completado |
| 5 | Barra de progreso y session_state | Completado |
| 6 | Pruebas, manejo de errores y deploy | Completado |
| 7 | Documentacion tecnica y refinamiento UI/UX | Completado |
