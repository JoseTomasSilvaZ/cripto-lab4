from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64
from utils import format_key

def tripledes_encrypt(key, iv, plaintext):
    cipher = DES3.new(format_key(key, 24), DES3.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), DES3.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode('utf-8')

def tripledes_decrypt(key, iv, encrypted_text):
    cipher = DES3.new(format_key(key, 24), DES3.MODE_CBC, iv)
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    decrypted_text = unpad(cipher.decrypt(encrypted_text_bytes), DES3.block_size)
    return decrypted_text.decode('utf-8')
