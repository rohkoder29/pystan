import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# actual date and time
now = datetime.now()

# email content placeholder
content = ''

# extracting Hacker News Stories
def extract_news(url):
    cnt = ''
    cnt += '<br>\n<strong>HackerNews Top Stories:</strong>\n<br>' + '-'*35 + '\n<br>\n'
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    for idx, tag in enumerate(soup.find_all('td', 
                                            attrs={'class': 'title', 
                                                   'valign': ''}), start=1):
        cnt += (f"{str(idx):>2}. {tag.text}\n<br>\n") if tag.text != "More" else ""
    return cnt


cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += (f"\n<br>{'-'*35}<br>")
content += ("<br><br>End of message")

print("Composing Email...")

# email composition parameters
SERVER = 'smtp.gmail.com'   # for gmail accounts
PORT = 587
FROM = 'darsontomus@gmail.com'
TO = ['tomwinchester98@gmail.com',
      'dyvador.p06@yahoo.com',
      'donsten_rohko@outlook.com']
# 
PASS = ''

# email body
msg = MIMEMultipart()
# dynamic title (to avoid emails being folded)
msg['Subject'] = f"[Automated Email] | Top Stories from HN on {now.day}/{now.month:>02}/{now.year}"
msg['From'] = FROM
msg['To'] = ", ".join(TO)
msg.attach(MIMEText(content, 'html'))

# email sending
print("Initializing server...")
server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP_SSL(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)

server.send_message(msg, FROM, TO)
print("Email successfully sent!")

print("Closing server...")
server.quit()
