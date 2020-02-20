from email import encoders
from email.mime.base import MIMEBase

from Secrets import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path = '1rivet/'
cc = 'btech.utu@gmail.com'
bcc = 'patelvini136@gmail.com'
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = email
msg['Subject'] = 'Sent using script'
body = """Hi,

This is just a test email."""
msg.attach(MIMEText(body, 'plain'))
filename = "ProcessLog.log"
attachment = open(path + filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text_msg = msg.as_string()
server.sendmail(email, [email, cc, bcc], text_msg)
server.quit()
