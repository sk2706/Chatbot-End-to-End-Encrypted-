from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 16
key = b'ThisIsASecretKey'  # Must be 16, 24, or 32 bytes

def pad(msg):
    return msg + (BLOCK_SIZE - len(msg) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(msg) % BLOCK_SIZE)

def unpad(msg):
    return msg[:-ord(msg[len(msg)-1:])]

def encrypt(raw):
    raw = pad(raw)
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(raw.encode('utf-8'))
    return base64.b64encode(enc).decode('utf-8')

def decrypt(enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(enc).decode('utf-8')
    return unpad(dec)
