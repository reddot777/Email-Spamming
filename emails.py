import smtplib
from email.message import EmailMessage
from concurrent.futures import ThreadPoolExecutor

ascii = """
▓█████   ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█   ▀ ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒███   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██
░▒████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ░ ░  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
   ░   ░  ░  ░  ░░         ░   ▒   ░      ░
   ░  ░      ░                 ░  ░       ░

made by reddot777
"""

print("\n", ascii)


sender_email = input("SENDER EMAIL  --> ")
app_password = input("APP PASSWORD -->  ")
target_email = input("TARGET EMAIL --> ")
subject_email = input("SUBJECT --> ")
body_email = input("BODY --> ")
thread = int(input("THREAD -->"))


def send_email(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["to"] = to
    msg["subject"] = subject
    email = sender_email
    password = app_password
    msg["from"] = email

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        for x in range(thread):
            executor.submit(send_email, target_email, subject_email, body_email)
            print(f"{x + 1} EMAIL SENT...")


































