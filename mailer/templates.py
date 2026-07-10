import random

SUBJECTS = [
    "Pregunta rapida para {first_name}",
    "Idea para {company}",
    "{first_name}, consulta breve",
    "Seguimiento sobre algo relevante para {company}",
    "Ideas para el equipo de {company}",
    "Hola {first_name}, queria compartirte algo",
    "Contactando a {company}",
]

OPENERS = [
    "Espero que te encuentres bien.",
    "Voy al grano.",
    "Te escribo porque creo que esto es relevante para tu trabajo.",
    "Vi tu perfil y queria conectar.",
    "Te contacto directamente porque creo que puede interesarte.",
]

BODIES = [
    "Estoy contactando a equipos de tu industria para compartir una propuesta que podria ser util para {company}.",
    "Por el tipo de trabajo que hace {company}, pense que valia la pena escribirte directamente.",
    "Estamos compartiendo una solucion sencilla para equipos como {company}, y queria saber si tiene sentido para ustedes.",
    "Vi informacion publica de {company} y pense que esta idea podria ser relevante para tu equipo.",
]

CLOSINGS = [
    "Estarias abierto a una llamada rapida?",
    "Con gusto comparto mas detalles si te interesa.",
    "Avisame si es relevante, sin compromiso.",
    "Si tiene sentido, puedo enviarte mas informacion.",
    "Te parece bien si te comparto mas detalles?",
]

def render_template(contact: dict) -> tuple:
    first = contact.get("First Name", "estimado")
    company = contact.get("Company Name", "su empresa")

    subject = random.choice(SUBJECTS).format(first_name=first, company=company)
    opener = random.choice(OPENERS)
    body_line = random.choice(BODIES).format(company=company)
    closing = random.choice(CLOSINGS)

    body = (
        f"Hola {first},\n\n"
        f"{opener}\n\n"
        f"{body_line}\n\n"
        f"{closing}\n\n"
        "Saludos,\n"
        "Amairani Rosales\n\n"
        "Si prefieres que no vuelva a contactarte, respondeme con 'baja' y lo respeto."
    )
    return subject, body
