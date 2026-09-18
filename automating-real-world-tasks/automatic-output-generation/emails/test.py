from email.message import EmailMessage
import os.path
import smtplib
import mimetypes
import getpass

#obtener password de uenta de email
mail_pass = getpass.getpass('Password? ')

mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)

#enviar correo con adjunto
attachment_path = "./attachments/bobby.jpeg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)

if mime_type is not None:
    mime_type, mime_subtype = mime_type.split('/', 1)

    message = EmailMessage()
    sender = "me@example.com"
    recipient = "you@example.com"
    body = """Hey there!

    I'm learning to send emails using Python!"""

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
    message.set_content(body)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
    print(message)
    mail_server.login(sender, mail_pass) #Code 235 2.7.0  Authentication Succeeded
    mail_server.send_message(message) #The send_message method returns a dictionary of any recipients that weren’t able to receive the message
    mail_server.quit()