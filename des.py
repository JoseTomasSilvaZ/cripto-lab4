from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64
from utils import format_key

def des_encrypt(key, iv, plaintext):
    cipher = DES.new(format_key(key, 8), DES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode('utf-8')

def des_decrypt(key, iv, encrypted_text):
    cipher = DES.new(format_key(key, 8), DES.MODE_CBC, iv)
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    decrypted_text = unpad(cipher.decrypt(encrypted_text_bytes), DES.block_size)
    return decrypted_text.decode('utf-8')
