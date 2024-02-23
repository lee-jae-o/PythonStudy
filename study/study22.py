import base64

def encrypt(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    encrypted_text = encoded_bytes.decode("utf-8")
    return encrypted_text

def decrypt(encrypted_text):
    decoded_bytes = base64.b64decode(encrypted_text.encode("utf-8"))
    decrypted_text = decoded_bytes.decode("utf-8")
    return decrypted_text

def main():
    user_input = input("Enter a message to encrypt: ")
    
    encrypted_message = encrypt(user_input)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()