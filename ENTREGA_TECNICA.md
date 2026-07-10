# Entrega tecnica

## Proyecto

Mass Mailer es una aplicacion Streamlit para cargar contactos exportados desde Apollo, filtrar correos verificados, generar plantillas personalizadas y enviar correos con SendGrid.

## Stack

- Python
- Streamlit
- Pandas
- OpenPyXL
- SendGrid

## Archivos principales

- `app.py`: interfaz principal, flujo de carga, vista previa, confirmacion de envio, barra de progreso y resultados.
- `mailer/loader.py`: lectura de CSV/XLS/XLSX, validacion de columnas y filtrado de contactos verificados.
- `mailer/templates.py`: generacion aleatoria de asuntos, aperturas, cuerpos y cierres.
- `mailer/sender.py`: envio con SendGrid, manejo de errores por contacto y delay aleatorio.
- `.streamlit/secrets.toml.example`: ejemplo de configuracion local sin credenciales reales.
- `requirements.txt`: dependencias necesarias para ejecucion local y despliegue.

## Configuracion requerida

La aplicacion requiere estos secretos:

```toml
SENDGRID_API_KEY = "tu_api_key_de_sendgrid"
SENDGRID_FROM_EMAIL = "informaitesi@gmail.com"
SENDGRID_FROM_NAME = "Amairani Rosales"
REPLY_TO_EMAIL = "informaitesi@gmail.com"
```

En Streamlit Cloud se configuran desde `Settings > Secrets`.

## Formato esperado del archivo de contactos

Columnas requeridas:

- `First Name`
- `Last Name`
- `Email`
- `Email Status`

Columna opcional usada para personalizacion:

- `Company Name`

Ejemplo:

```csv
First Name,Last Name,Email,Email Status,Company Name
Paulina,Test,correo@example.com,verified,Test Company
```

## Criterios de aceptacion

- La app carga archivos CSV, XLS y XLSX.
- La app muestra solo contactos con `Email Status = verified`.
- La app permite generar una vista previa antes del envio.
- La app bloquea el envio si no hay contactos, si SendGrid no esta configurado o si no se confirma la lista.
- La app permite limitar la cantidad de correos antes de iniciar.
- La app muestra progreso y tabla final de resultados.
- Las credenciales no estan escritas en el codigo.

## Pendiente operativo

- Crear o entrar a la cuenta SendGrid de `informaitesi@gmail.com`.
- Verificar `informaitesi@gmail.com` como Single Sender.
- Crear una API Key nueva.
- Configurar los secretos en Streamlit Cloud.
- Borrar o regenerar cualquier API Key anterior que haya sido compartida.
- Para mejorar entregabilidad, autenticar un dominio propio en SendGrid con SPF, DKIM y DMARC.
