############################################
# THIS IS A BASIC MAILING CLIENT IN PYTHON #
############################################


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet

# 1. create a connection to the smtp server
address = "smtp.gmail.com"
port = 465
server = smtplib.SMTP_SSL(address, port)

# 2. start the service (the whole process)
server.ehlo()

# 3. login to your account (sender)
sender_email = "darsontomus@gmail.com"
## decrypt password from the encrypted file
file_path = "password.txt"
key_file = "passkey.key"

with open(key_file, 'rb') as encryption_key:
    key = encryption_key.read()

fernet = Fernet(key)

with open(file_path, 'rb') as encrypted_file:
    encrypted_password = encrypted_file.read()

password = fernet.decrypt(encrypted_password).decode("UTF-8")
server.login(sender_email, password.strip())

# 4. create the actual mail content 
receiver_email = "fg99.wd1ny@slmail.me"
## we'll extract the message from a text file
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Python Mailing Client"

with open("message.txt", "r") as stream:
    message = stream.read()

msg.attach(MIMEText(message, "plain"))

## we may also attach an image
img_path = "vim_cheat_sheet.png"
attachment = open(img_path, "rb")

## now create a payload object for our attachment
pload = MIMEBase("application", "octet-stream")
pload.set_payload(attachment.read())

## we also need to encode it and add a header
encoders.encode_base64(pload)
pload.add_header("Content-Disposition", "attachment; filename='Vim Cheat Sheet'")
## and finally attach it
msg.attach(pload)


text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)













