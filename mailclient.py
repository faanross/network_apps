import smtplib
import hashlib 
import base64
from email import encoders

server = smtplib.SMTP('smtp-mail.outlook.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    encrypted_password = f.read()

decoded_password = base64.b64decode(encrypted_password)
sha256 = hashlib.sha256()
sha256.update(decoded_password)
decrypted_password = sha256.hexdigest()


server.login('mail@example.com', decrypted_password) # instead of adding real password here, save as seperate encrytped file, import to a variable and use that here. 



