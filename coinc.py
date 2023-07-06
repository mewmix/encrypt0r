import coincurve

def encrypt_message(public_key, message):
    encrypted = public_key.encrypt(message.encode())
    return encrypted.hex()

# Example usage
recipient_public_key_hex = '0362c19c3b0ebce13bdf75d7757e8d48f89a4e6f3761941ef1a15b3f0c7c3db136'
message_to_encrypt = 'Hello, recipient! This is a secret message.'

recipient_public_key = coincurve.PublicKey.from_hex(recipient_public_key_hex)
encrypted_message = encrypt_message(recipient_public_key, message_to_encrypt)

print(f"Encrypted message: {encrypted_message}")
