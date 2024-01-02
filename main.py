import streamlit as st

from utils import (
    caesar_encryption, caesar_decryption, rode_encryption, rode_decryption,
    rot13_encryption, rot13_decryption, encrypt_vigenere_cipher, decrypt_vingenere_cipher
)

st.set_page_config(page_title="Chiper App", page_icon="🧊", layout="centered", initial_sidebar_state="expanded", menu_items={
        'About': "# This is a Chiper App. This is an *extremely* cool app!"
    })

st.title('Cipher App')
st.caption('Made by: :blue[Muhammad Faridan Sutariya]')


cipher_options = ['Caesar Cipher', 'Rode', 'Rot13', 'Vigenere']
selected_cipher = st.selectbox('Select Cipher:', cipher_options)

def process_caesar_cipher(message, option, key):
    if option == 'Encryption':
        return caesar_encryption(message.upper(), key)
    else:
        return caesar_decryption(message.upper(), key)

def process_rode_cipher(message, option):
    if option == 'Encryption':
        return rode_encryption(message.upper())
    else:
        return rode_decryption(message.upper())

def process_rot13_cipher(message, option):
    if option == 'Encryption':
        return rot13_encryption(message.upper())
    else:
        return rot13_decryption(message.upper())

def process_vigenere_cipher(message, option, key):
    if option == 'Encryption':
        return encrypt_vigenere_cipher(message.upper(), key)
    else:
        return decrypt_vingenere_cipher(message.upper(), key)

def is_alpha_string(s):
    return s.isalpha()

# File upload feature
uploaded_file = st.file_uploader('Upload file (each  text must be separated by a semicolon)', type=['csv', 'txt'])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()

    file_contents = uploaded_file.getvalue().decode("utf-8")
    messages = file_contents.split(';')
    messages = [message.strip() for message in messages]

    key = None
    if selected_cipher == 'Caesar Cipher':
        key = st.number_input('Key:', value=1)
    elif selected_cipher == "Vigenere":
        key = st.text_input('Key:', help="Example key: GOKIL or WTFIND")
        if not key:
            st.warning('Key cannot be empty for Vigenere Cipher!')
        elif not key.isalpha():
            st.warning('Key for Vigenere Cipher must contain only alphabetic characters!')

    option = st.radio('Select Option:', ('Encryption', 'Decryption'))

    if st.button('Process All'):
        if selected_cipher == 'Vigenere' and (not key or not key.isalpha()):
            st.warning('Key cannot be empty and must contain only alphabetic characters for Vigenere Cipher!')
        else:
            processed_output = []
            for message in messages:
                if selected_cipher == 'Caesar Cipher':
                    result = process_caesar_cipher(message.replace(',', ''), option, key)
                elif selected_cipher == 'Rode':
                    result = process_rode_cipher(message.replace(',', ''), option)
                elif selected_cipher == 'Rot13':
                    result = process_rot13_cipher(message.replace(',', ''), option)
                else:
                    result = process_vigenere_cipher(message.replace(',', ''), option, key)
                
                processed_output.append((message.replace(',', ''), result))

            for input_msg, output_msg in processed_output:
                st.markdown(f'Input: {input_msg}\nProcessed Output: \n```\n{output_msg}\n```')

            if processed_output:
                output_text = "\n\n".join([f'Input: {input_msg}\nProcessed Output: \n{output_msg}' for input_msg, output_msg in processed_output])
                st.download_button(
                    label="Download Processed Results",
                    data=output_text,
                    file_name=f"processed_results_{selected_cipher.lower()}.txt",
                    mime="text/plain"
                )

# Manual input
else:
    st.subheader(f'{selected_cipher} Cipher')
    option = st.radio('Select Option:', ('Encryption', 'Decryption'))
    message = st.text_input('Enter  Text:')

    if selected_cipher == 'Vigenere':
        key = st.text_input('Key:', help="Example key: GOKIL or WTFIND")
        if not key:
            st.warning('Key cannot be empty for Vigenere Cipher!')
        elif not key.isalpha():
            st.warning('Key for Vigenere Cipher must contain only alphabetic characters!')

        # Automatically process the input when both message and key are provided
        if st.button('Encrypt' if option == 'Encryption' else 'Decrypt') and message and key.isalpha():
            processed_text = process_vigenere_cipher(message, option, key)
            st.markdown(f'Processed Text: \n```\n{processed_text}\n```')
    elif selected_cipher == 'Caesar Cipher':
        key = st.number_input('Key:', value=1)
        
        if st.button('Encrypt' if option == 'Encryption' else 'Decrypt'):
            if not message:
                st.warning('Please enter a  Text!')
            elif not message.isalpha():
                 st.warning(' Text must contain only alphabetic characters!')
            else:
                processed_text = process_caesar_cipher(message, option, key)
                st.markdown(f'Processed Text: \n```\n{processed_text}\n```')
    elif selected_cipher in ['Rode', 'Rot13']:
        if st.button('Encrypt' if option == 'Encryption' else 'Decrypt'):
            if not message:
                st.warning('Please enter a  Text!')
            elif not message.isalpha():
                 st.warning(' Text must contain only alphabetic characters!')
            else:
                if selected_cipher == 'Rode':
                    processed_text = process_rode_cipher(message, option)
                else:
                    processed_text = process_rot13_cipher(message, option)

                st.markdown(f'Processed Text: \n```\n{processed_text}\n```')
