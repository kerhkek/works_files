def caesar_encrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

with open('secret.txt', 'r', encoding='utf-8') as file:
    secret_text = file.read()

encrypted_text = caesar_encrypt(secret_text)

with open('encrypted.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

with open('encrypted.txt', 'r', encoding='utf-8') as file:
    encrypted_content = file.read()

decrypted_text = caesar_decrypt(encrypted_content)

with open('decrypted.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_text)