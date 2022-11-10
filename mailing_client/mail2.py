################################################
# THIS IS A SECOND FORM FOR THE MAILING CLIENT #
################################################


# imports
from smtplib import SMTP_SSL
from email.message import EmailMessage
from ssl import create_default_context
from cryptography.fernet import Fernet


sender_email = "darsontomus@gmail.com"
## we gonna have to decrypt the password first
file_path = "password.txt"
key_file = "passkey.key"
### read the file to retrieve the key
with open(key_file, "rb") as encryption_key:
    key = encryption_key.read()
### put it into the Fernet object
fernet = Fernet(key)
### read the file containing the actual password
with open(file_path, "rb") as encrypted_file:
    encrypted_password = encrypted_file.read()
### decrypt it
password = fernet.decrypt(encrypted_password).decode("UTF-8")
##
receiver_email = "fg99.wd1ny@slmail.me"

# the content of the email
subject = "Check out my new form of the Mailing Client"
## the body is gonna be this file, so we'll open it
with open("mail2.py", "r") as stream:
    body = stream.read()

## now we create the email
mail = EmailMessage()
mail["From"] = sender_email
mail["To"] = receiver_email
mail["Subject"] = subject
mail.set_content(body)

## let's add a layer of security
secure = create_default_context()

# finally send the email
with SMTP_SSL("smtp.gmail.com", 465, context=secure) as smtp:
    ## enable connection to the server
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, mail.as_string())

