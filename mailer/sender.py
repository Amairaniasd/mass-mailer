import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(smtp_config, to_email, subject, body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_config["user"]
    msg["To"] = to_email
    msg["X-Mailer"] = "Microsoft Outlook 16.0"
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_config["host"], smtp_config["port"]) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_config["user"], smtp_config["password"])
        server.sendmail(smtp_config["user"], to_email, msg.as_string())

def send_batch(contacts_df, smtp_config, render_fn, progress_callback=None):
    results = []
    total = len(contacts_df)
    for i, row in contacts_df.iterrows():
        contact = row.to_dict()
        subject, body = render_fn(contact)
        try:
            send_email(smtp_config, contact["Email"], subject, body)
            results.append({"Correo": contact["Email"], "Asunto": subject, "Estado": "Enviado"})
        except Exception as e:
            results.append({"Correo": contact["Email"], "Asunto": subject, "Estado": f"Error: {e}"})
        if progress_callback:
            progress_callback((i + 1) / total)
        time.sleep(random.uniform(3, 8))
    return results
