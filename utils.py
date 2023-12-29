import streamlit as st


# Caesar Cipher Functions
def caesar_encryption(message, key):
    if not key:
        return "Key cannot be empty for Caesar Cipher!"
    
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            shift = (ord(char) - ord('A') + key) % 26
            encrypted_text += chr(ord('A') + shift)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decryption(message, key):
    if not key:
        return "Key cannot be empty for Caesar Cipher!"
    
    decrypted_text = ""
    for char in message:
        if char.isalpha():
            shift = (ord(char) - ord('A') - key) % 26
            decrypted_text += chr(ord('A') + shift)
        else:
            decrypted_text += char
    return decrypted_text

# Rode Cipher Functions
def rode_encryption(message):
    key = 13
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            temp = ord(char) + key
            if temp > ord('Z'):
                temp -= 26
            encrypted_text += chr(temp)
        else:
            encrypted_text += char
    return encrypted_text

def rode_decryption(message):
    key = 13
    decrypted_text = ""
    for char in message:
        if char.isalpha():
            temp = ord(char) - key
            if temp < ord('A'):
                temp += 26
            decrypted_text += chr(temp)
        else:
            decrypted_text += char
    return decrypted_text

# Rot13 Cipher Functions
def rot13_encryption(message):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            temp = ord(char) + 13
            if char.islower() and temp > ord('z'):
                temp -= 26
            elif char.isupper() and temp > ord('Z'):
                temp -= 26
            encrypted_text += chr(temp)
        else:
            encrypted_text += char
    return encrypted_text

def rot13_decryption(message):
    decrypted_text = ""
    for char in message:
        if char.isalpha():
            temp = ord(char) - 13
            if char.islower() and temp < ord('a'):
                temp += 26
            elif char.isupper() and temp < ord('A'):
                temp += 26
            decrypted_text += chr(temp)
        else:
            decrypted_text += char
    return decrypted_text

# Vigenere Cipher Functions
def encrypt_vigenere_cipher(text, keyword):
    if not keyword:
        st.warning("Key cannot be empty for Vigenere Cipher!")
        return
    
    result = ""
    keyword_length = len(keyword)
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shifted = ord(keyword[key_index % keyword_length]) - ord('A')
            alphabet = ord(char) - ascii_offset
            alphabet_shifted = (alphabet + keyword_shifted) % 26
            char = chr(alphabet_shifted + ascii_offset)
            key_index += 1
        result += char

    return result

def decrypt_vingenere_cipher(text, keyword):
    if not keyword:
        st.warning("Key cannot be empty for Vigenere Cipher!")
        return
    
    result = ""
    keyword_length = len(keyword)
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shifted = ord(keyword[key_index % keyword_length]) - ord('A')
            alphabet = ord(char) - ascii_offset
            alphabet_shift_reversed = (alphabet - keyword_shifted) % 26
            char = chr(alphabet_shift_reversed + ascii_offset)
            key_index += 1
        result += char

    return result
