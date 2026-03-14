import imaplib
import email
from email.header import decode_header

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

                
                print("From:", msg["From"])
                print("Subject:", msg["Subject"])
                print()

                # Extract body
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            print("Body:\n", body)
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                    print("Body:\n", body)
        mail.logout()
    except Exception as e:
        print("Failed to read inbox, error code: ")
        print(e)

fetch_inbox()