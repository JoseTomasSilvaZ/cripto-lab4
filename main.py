from aes import aes_encrypt, aes_decrypt
from des import des_encrypt, des_decrypt
from tripledes import tripledes_encrypt, tripledes_decrypt
from utils import format_key

def main():
    method = input("Select encryption method (AES/DES/3DES): ").strip().upper()
    
    if method == "AES":
        raw_key = input("Key (32 chars, in any other case, will be formatted): ").encode()
        key = format_key(raw_key, 32)
        print(f"Final key used (32 bytes): {key}")
        
        iv = input("IV (exactly 16 chars): ").encode()
        if len(iv) != 16:
            print("AES IV must be exactly 16 chars.")
            return
        
        action = input("Encrypt or decrypt? (e/d): ").strip().lower()
        if action == "e":
            plaintext = input("Plain text: ")
            encrypted_text = aes_encrypt(key, iv, plaintext)
            print(f"Encrypted text (base64): {encrypted_text}")
        elif action == "d":
            encrypted_text = input("Encrypted text (base64): ")
            try:
                decrypted_text = aes_decrypt(key, iv, encrypted_text)
                print(f"Decrypted text: {decrypted_text}")
            except ValueError as e:
                print("Decryption failed:", e)

    elif method == "DES":
        raw_key = input("Key (8 chars, in any other case, will be formatted): ").encode()
        key = format_key(raw_key, 8)
        print(f"Final key used (8 bytes): {key}")
        
        iv = input("IV (exactly 8 chars): ").encode()
        if len(iv) != 8:
            print("DES IV must be exactly 8 chars.")
            return
        
        action = input("Encrypt or decrypt? (e/d): ").strip().lower()
        if action == "e":
            plaintext = input("Plain text: ")
            encrypted_text = des_encrypt(key, iv, plaintext)
            print(f"Encrypted text (base64): {encrypted_text}")
        elif action == "d":
            encrypted_text = input("Encrypted text (base64): ")
            try:
                decrypted_text = des_decrypt(key, iv, encrypted_text)
                print(f"Decrypted text: {decrypted_text}")
            except ValueError as e:
                print("Decryption failed:", e)

    elif method == "3DES":
        raw_key = input("Key (24 chars, in any other case, will be formatted): ").encode()
        key = format_key(raw_key, 24)
        print(f"Final key used (24 bytes): {key}")
        
        iv = input("IV (exactly 8 chars): ").encode()
        if len(iv) != 8:
            print("3DES IV must be exactly 8 chars.")
            return
        
        action = input("Encrypt or decrypt? (e/d): ").strip().lower()
        if action == "e":
            plaintext = input("Plain text: ")
            encrypted_text = tripledes_encrypt(key, iv, plaintext)
            print(f"Encrypted text (base64): {encrypted_text}")
        elif action == "d":
            encrypted_text = input("Encrypted text (base64): ")
            try:
                decrypted_text = tripledes_decrypt(key, iv, encrypted_text)
                print(f"Decrypted text: {decrypted_text}")
            except ValueError as e:
                print("Decryption failed:", e)

    else:
        print("Invalid encryption method. Please select AES, DES, or 3DES.")

if __name__ == "__main__":
    main()
