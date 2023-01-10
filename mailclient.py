import smtplib
import hashlib 
import base64
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp-mail.outlook.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    encrypted_password = f.read()

decoded_password = base64.b64decode(encrypted_password)
sha256 = hashlib.sha256()
sha256.update(decoded_password)
decrypted_password = sha256.hexdigest()


server.login('cagefighter69@preston.com', decrypted_password) # instead of adding real password here, save as seperate encrytped file, import to a variable and use that here. 

msg = MIMEMultipart()
msg['From'] = 'Kipland Dynamite'
msg['To'] = 'lawfawnduh@gmail.com'
msg['Subject'] = 'Your sandy hair floats in the air...'

with open('mesasge.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'nunchucks.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('cagefighter69@preston.com', 'lawfawnduh@gmail.com', text)