from eth_account import Account
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os


def decode_message_with_private_key(private_key_path, encrypted_message):
    # Read the private key from the file
    with open(private_key_path, 'rb') as file:
        private_key = file.read()

    # Derive the encryption key from the private key using PBKDF2
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

    # Decrypt the message using Fernet decryption
    cipher_suite = Fernet(encoded_key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

    return decrypted_message


encrypted_message = b'gAAAAABkpKpJmlKitIAHl3wIDil5r7eXgwZVPMeGcO72OXKL4QOE7wZCyD6va8p_qNjTCYhdAHWWbfrFMzVbgdKsOEJaCR_FEw=='
private_key_path = 'key.txt'  # Provide the path to the key.txt file

# Call the decode_message_with_private_key function
decoded_message = decode_message_with_private_key(private_key_path, encrypted_message)

# Print the decoded message
print("Decoded Message:", decoded_message)
