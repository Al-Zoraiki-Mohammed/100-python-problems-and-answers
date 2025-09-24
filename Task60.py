"""Task60"""

def encrypt_text(text, encryption_key = 2):
    encrypted_text = ""
    for letter in text:
        encrypted_letter = chr((ord(letter) + encryption_key))
        encrypted_text += encrypted_letter
    return encrypted_text


def decrypt_text(encrypted_text, encryption_key = 2):
    decrypted_text = ""
    for letter in encrypted_text:
        decrypted_letter = chr((ord(letter) - encryption_key))
        decrypted_text += decrypted_letter
    return decrypted_text


def print_result(text):
    print(f'Text before encryption: {text}')
    print(f'Text after encryption: {encrypt_text(text)}')
    print(f'Text after decryption: {decrypt_text(encrypt_text(text))}')

 
if __name__ == "__main__":
    text = input('Type text to encrypt: ')
    encryption_key = 2
    encrypted_text = encrypt_text(text, encryption_key)
    decrypted_text = decrypt_text(encrypted_text, encryption_key)
    print(f'Text before encryption: {text}')
    print(f'Text after encryption: {encrypted_text}')
    print(f'Text after decryption: {decrypted_text}')
    


    