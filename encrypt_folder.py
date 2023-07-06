from cryptography.fernet import Fernet
import os

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            with open(file_path, 'rb') as file:
                data = file.read()

            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)

            encrypted_file_path = file_path + '.encrypted'
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            key_file_path = file_path + '.key'
            with open(key_file_path, 'wb') as key_file:
                key_file.write(key)

            # Remove the original file
            os.remove(file_path)

# Generate a random encryption key
key = Fernet.generate_key()

# Encrypt a folder and remove original files
folder_path = 'vault'
encrypt_folder(folder_path, key)
