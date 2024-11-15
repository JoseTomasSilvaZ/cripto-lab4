from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from utils import format_key

def aes_encrypt(key, iv, plaintext):
    cipher = AES.new(format_key(key, 32), AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode('utf-8')

def aes_decrypt(key, iv, encrypted_text):
    cipher = AES.new(format_key(key, 32), AES.MODE_CBC, iv)
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    decrypted_text = unpad(cipher.decrypt(encrypted_text_bytes), AES.block_size)
    return decrypted_text.decode('utf-8')
