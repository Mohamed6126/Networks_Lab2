import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tkinter as tk
from tkinter import filedialog


def send_mail(send_email, receiver_email, sender_pass, subject, body, filepath):
    try:
        mail = MIMEMultipart()
        mail["From"] = send_email
        mail["To"] = receiver_email
        mail["Subject"] = subject

        mail.attach(MIMEText(body, "plain"))
        with open(filepath, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())

        encoders.encode_base64(part)
        filename = os.path.basename(filepath)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        mail.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_pass)
        
        server.sendmail(sender_email, receiver_email, mail.as_string())
    except Exception as e:
        print("Error sending mail, Error code: ")
        print(e)


sender_email = input("From: ")
receiver_email = input("To: ")
subject = input("Subject: ")
body = input("Message: ")
sender_pass = "fmisqojvvkwadyvc"

root = tk.Tk()
root.withdraw() 
filepath = filedialog.askopenfilename(
    title="Select attachment",
    filetypes=[("All files", "*.*")]
)
send_mail(sender_email, receiver_email, sender_pass, subject, body, filepath)


