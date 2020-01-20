import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import email_tweaks


class Postman:
    def __init__(self, receiver_email, body, html):
        self.subject = email_tweaks["subject"]
        self.body = body
        self.sender_email = email_tweaks["master_email"]
        self.receiver_email = receiver_email
        self.password = email_tweaks["password"]

        # Create a multipart message and set headers
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = receiver_email
        self.message["Subject"] = self.subject
        self.message["Bcc"] = receiver_email

        # Add body to email
        self.message.attach(MIMEText(body, "plain"))
        if html:
            self.message.attach(MIMEText(html, 'html'))
        self.text = self.message.as_string()

    # Log in to server using secure context and send email
    def deliver_article(self):
        with smtplib.SMTP(email_tweaks["SMTP"], email_tweaks["port"]) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.text)
