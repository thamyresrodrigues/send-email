import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# module settings / send email
port = 587
smtp_server = "smtp.gmail.com"

sender_email = "your_email@email.com"
receiver_email = "other_email@email.com"
password = input("Type your password and press enter:")  # your password

msg = MIMEMultipart()
msg['Subject'] = '[TEST]'  # subject
msg['From'] = sender_email
msg['To'] = receiver_email

# customizable message
html = """
<html>
    <body>
        <p>E-mail automático ;)</p>
        <p>Teste de envio de e-mails em python</>
        <p>Att: Amy.</p>
    </body>
</html>"""

part2 = MIMEText(html, "html")
msg.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )
    print('EMAIL SENT.')

