import random

SUBJECTS = [
    "Pregunta rapida para {first_name}",
    "Esto podria interesarte, {first_name}",
    "{first_name}, vale 2 minutos?",
    "Seguimiento sobre algo relevante para {company}",
    "Ideas para el equipo de {company}",
    "Hola {first_name}, tenia una idea",
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
    "Hemos trabajado con equipos de tu industria en algo que creo que puede ayudar genuinamente a {company}.",
    "Dado tu rol en {company}, pense que esto te seria util.",
    "Ayudamos a empresas como {company} a resolver un problema muy especifico que creo que aplica en tu caso.",
    "He estado siguiendo lo que hace {company} y queria compartir algo util.",
]

CLOSINGS = [
    "Estarias abierto a una llamada rapida?",
    "Con gusto comparto mas detalles si te interesa.",
    "Avisame si es relevante, sin compromiso.",
    "Vale una llamada de 15 minutos?",
    "Tienes disponibilidad para una llamada esta semana?",
]

def render_template(contact: dict) -> tuple:
    first = contact.get("First Name", "estimado")
    company = contact.get("Company Name", "su empresa")

    subject = random.choice(SUBJECTS).format(first_name=first, company=company)
    opener = random.choice(OPENERS)
    body_line = random.choice(BODIES).format(company=company)
    closing = random.choice(CLOSINGS)

    body = f"Hola {first},\n\n{opener}\n\n{body_line}\n\n{closing}\n\nSaludos,\n[TU NOMBRE]"
    return subject, body
