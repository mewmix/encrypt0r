from eth_account import Account
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os 

# Generate a new Ethereum account
account = Account.create()

# Get the private key from the account
private_key = account.privateKey
# Derive a symmetric encryption key from the private key using PBKDF2
salt = b'salt'  # You can choose your own salt value
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
derived_key = kdf.derive(private_key)

# Encode the derived key to base64
encoded_key = base64.urlsafe_b64encode(derived_key)

# Save the key to a file
with open('key.txt', 'wb') as file:
    file.write(encoded_key)

# Encrypt the message using Fernet encryption
message = 'Hello, World!'
cipher_suite = Fernet(encoded_key)
print(Fernet(encoded_key))
encrypted_message = cipher_suite.encrypt(message.encode())

# Decrypt the message using Fernet decryption
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

# Print the private key, encrypted message, and decrypted message
print("Private Key:", private_key.hex())
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
