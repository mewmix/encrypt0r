import coincurve

def decrypt_message(private_key, encrypted_message):
    encrypted_bytes = bytes.fromhex(encrypted_message)
    decrypted = private_key.decrypt(encrypted_bytes)
    return decrypted.decode()

# Example usage
recipient_private_key_hex = 'c2b9a830a8f01a1b14f5e9a3d4a1fd579042b046d8aa870b8f9dd3f4f9541b16'
encrypted_message = '295e8d0cfc8f75912e556b51c08b35b8c6c0b1356ee7e3756ed68300ef67764f'

recipient_private_key = coincurve.PrivateKey.from_hex(recipient_private_key_hex)
decrypted_message = decrypt_message(recipient_private_key, encrypted_message)

print(f"Decrypted message: {decrypted_message}")
