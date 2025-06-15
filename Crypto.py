from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode(), 16))
    return iv + ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), 16)
    return plaintext.decode()

key = b'This_is_a_key123'  # Must be 16, 24, or 32 bytes
message = input("Enter the data to encrypt: ")
encrypted = encrypt(message, key)
print("Encrypted (bytes):", encrypted)
decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
