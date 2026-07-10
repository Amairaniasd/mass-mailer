import random
import time

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(sendgrid_config, to_email, subject, body):
    message = Mail(
        from_email=(
            sendgrid_config["from_email"],
            sendgrid_config.get("from_name", sendgrid_config["from_email"]),
        ),
        to_emails=to_email,
        subject=subject,
        plain_text_content=body,
    )

    client = SendGridAPIClient(sendgrid_config["api_key"])
    response = client.send(message)
    if response.status_code >= 400:
        raise RuntimeError(f"SendGrid respondio con estado {response.status_code}")


def send_batch(contacts_df, sendgrid_config, render_fn, progress_callback=None):
    results = []
    total = len(contacts_df)

    for i, row in contacts_df.iterrows():
        contact = row.to_dict()
        subject, body = render_fn(contact)

        try:
            send_email(sendgrid_config, contact["Email"], subject, body)
            results.append({"Correo": contact["Email"], "Asunto": subject, "Estado": "Enviado"})
        except Exception as e:
            results.append({"Correo": contact["Email"], "Asunto": subject, "Estado": f"Error: {e}"})

        if progress_callback:
            progress_callback((i + 1) / total)

        time.sleep(random.uniform(3, 8))

    return results
