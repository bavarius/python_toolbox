import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

SMTP_ADDRESS = 'smtp.ionos.de'
SMTP_PORT = 587

server = smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT)
try:
    name="bavarius" # name to be displayed
    server.connect(SMTP_ADDRESS, SMTP_PORT)
    server.starttls()
    server.ehlo()
    server.login(os.environ['IONOS_FROM_EMAIL'], os.environ['IONOS_MAIL_PW'])
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Subject goes here"
    msg['From'] = os.environ['IONOS_FROM_EMAIL']
    msg['To'] = os.environ['TO_EMAIL']
    # E-mail body
    html = """\
                <html>
                  <body>
                    <p><span style="color: rgb(0,0,0);">Lieber {0},</span></p>
                   <p>
                      der Mail-Inhalt.
                    </p>
                    <p>LG,<br />
                    Ich
                    </p>
                    </body>
                </html>
                """.format(name.split()[0])
    msg.attach(MIMEText(html, 'html'))
    server.sendmail(os.environ['IONOS_FROM_EMAIL'], os.environ['TO_EMAIL'], msg.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
