###############################################
# THIS IS A THIRD FORM FOR THE MAILING CLIENT #
###############################################


# imports
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from ssl import create_default_context
from os.path import basename
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
subject = "Check out my third form of the Mailing Client"
content = "It's getting sharp, doesn't it?"

## now we create the email
mail = MIMEMultipart()
mail["From"] = sender_email
mail["To"] = receiver_email
mail["Subject"] = subject
body = MIMEText(content, "plain")
mail.attach(body)

# add an attachment
filename = "mail2.py"
with open(filename, "r") as file:
    attachment = MIMEApplication(file.read(), Name=basename(filename))
    attachment["Content-Disposition"] = f"attachment; filename={basename(filename)}"
mail.attach(attachment)

## let's add a layer of security
secure = create_default_context()

# send the email
## enable connection to the server
with SMTP_SSL("smtp.gmail.com", 465, context=secure) as smtp:
    ## login
    smtp.login(sender_email, password)
    ## actually send the mail
    smtp.sendmail(sender_email, receiver_email, mail.as_string())

