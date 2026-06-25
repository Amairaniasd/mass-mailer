# 📧 Mass Mailer

Aplicación web construida con **Python + Streamlit** para el envío masivo de correos personalizados, diseñada para evitar detección como spam mediante aleatorización de plantillas.

## Tecnologías
- Python 3.10+
- Streamlit
- Pandas
- smtplib (librería estándar de Python)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/mass-mailer.git
cd mass-mailer

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
streamlit run app.py
```

## Estructura del proyecto

```
mass-mailer/
├── app.py              # Aplicación principal
├── mailer/
│   ├── __init__.py
│   ├── loader.py       # Carga y validación de CSV
│   ├── templates.py    # Motor de plantillas aleatorizadas
│   └── sender.py       # Lógica de envío SMTP
├── requirements.txt
└── .gitignore
```

## Cronograma

| Semana | Entregable |
|--------|------------|
| 1 | Configuración del entorno y estructura base ✅ |
| 2 | Carga y validación de CSV con Pandas |
| 3 | Motor de aleatorización de plantillas |
| 4 | Integración UI de credenciales SMTP |
| 5 | Barra de progreso y session_state |
| 6 | Pruebas, manejo de errores y deploy |
| 7 | Documentación técnica y refinamiento UI/UX |
