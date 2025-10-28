from cryptography.fernet import Fernet

# Load or generate a key
def load_key():
    try:
        with open("chat.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("chat.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fernet = Fernet(key)

def encrypt_message(message: str) -> bytes:
    return fernet.encrypt(message.encode())

def decrypt_message(token: bytes) -> str:
    return fernet.decrypt(token).decode()
