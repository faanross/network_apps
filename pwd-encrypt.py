import hashlib
import base64

password = input("Enter password: ")

sha256 = hashlib.sha256()
sha256.update(password.encode())

encrypted_password = sha256.hexdigest()

encoded_password = base64.b64encode(encrypted_password.encode())

with open('password.txt', 'w') as f:
    f.write(encoded_password.decode())
print('Password encrypted and saved to password.txt')

# This password.txt can now be loaded into the mailclient.py (or other appropriate scripts) to ensure no cleartext is used
