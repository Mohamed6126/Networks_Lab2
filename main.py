import tkinter as tk
from tkinter import filedialog, messagebox
import send_email
import receive_email

def browse_file():
    filename = filedialog.askopenfilename()
    attachment.set(filename)

def send():
    try:
        send_email.send_mail(
            entry_sender.get(),
            entry_receiver.get(),
            send_email.sender_pass,
            entry_subject.get(),
            text_body.get("1.0", tk.END),
            attachment.get()
        )
        messagebox.showinfo("Success", "Email Sent!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def receive():
    try:
        email_body = receive_email.fetch_inbox()
        messagebox.showinfo("Latest Email", email_body)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Email Client")

attachment = tk.StringVar()

tk.Label(root, text="Sender Email").pack()
entry_sender = tk.Entry(root, width=40)
entry_sender.pack()

tk.Label(root, text="Receiver Email").pack()
entry_receiver = tk.Entry(root, width=40)
entry_receiver.pack()

tk.Label(root, text="Subject").pack()
entry_subject = tk.Entry(root, width=40)
entry_subject.pack()

tk.Label(root, text="Message").pack()
text_body = tk.Text(root, height=6, width=40)
text_body.pack()

tk.Button(root, text="Attach File", command=browse_file).pack()
tk.Label(root, textvariable=attachment).pack()

tk.Button(root, text="Send Email", command=send).pack(pady=5)
tk.Button(root, text="Receive Latest Email", command=receive).pack(pady=5)

root.mainloop()