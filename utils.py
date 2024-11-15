from Crypto.Random import get_random_bytes

def format_key(key, length=16):
    if len(key) < length:
        print(f"Key is too short. Adding {length - len(key)} random bytes to reach {length} bytes")
        key += get_random_bytes(length - len(key))
    elif len(key) > length:
        print(f"Key is too long. Truncating to {length} bytes")
    else:
        print("Correct length")
    return key[:length]
