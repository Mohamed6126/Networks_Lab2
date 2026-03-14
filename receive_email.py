import imaplib
import email
from email.header import decode_header
import os
import subprocess


imap_server = "imap.gmail.com"
email_address = "ma7amedhossam@gmail.com"
password = "fmisqojvvkwadyvc"
def fetch_inbox():
    try:
        mail = imaplib.IMAP4_SSL(imap_server, 993)
        mail.login(email_address, password)
        mail.select("INBOX")
        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()

        if not email_ids:
            print("Inbox is Empty!")
            return
        
        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                
                result = ""
                result += "From: " + str(msg["From"]) + "\n"
                result += "Subject: " + str(msg["Subject"]) + "\n\n"

                body = ""
                attachments = []

                if msg.is_multipart():

                    for part in msg.walk():
                        if part.get_content_type() == "text/plain" and part.get("Content-Disposition") is None:
                            body = part.get_payload(decode=True).decode()
                        if part.get("Content-Disposition") is not None:
                            filename = part.get_filename()

                            if filename:
                                filepath = os.path.join("attachments", filename)

                                os.makedirs("attachments", exist_ok=True)

                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                    subprocess.Popen(["xdg-open", filepath])

                                attachments.append(filename)
                else:
                    body = msg.get_payload(decode=True).decode()
                
        result += body
        mail.logout()
        return result
    except Exception as e:
        print("Failed to read inbox, error code: ")
        print(e)
