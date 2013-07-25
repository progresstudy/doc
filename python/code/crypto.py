import Crypto.Cipher.AES
import base64
from random import Random

key = "aEN0eGE2M05EZ0N2ajJVMQ=="

def _build_cipher(key, iv):
    """Make a 128bit AES CBC encode/decode Cipher object.
       Padding is handled internally."""
    return Crypto.Cipher.AES.new(key, IV=iv)


def encryptor(key):
    """Simple symmetric key encryption."""
    key = base64.b64decode(key)
    iv = '\0' * 16

    def encrypt(data):
        cipher = _build_cipher(key, iv)
        # Must pad string to multiple of 16 chars
        padding = (16 - len(data) % 16) * " "
        v = cipher.encrypt(data + padding)
        del cipher
        v = base64.b64encode(v)
        return v

    return encrypt


def decryptor(key):
    """Simple symmetric key decryption."""
    key = base64.b64decode(key)
    iv = '\0' * 16

    def decrypt(data):
        data = base64.b64decode(data)
        cipher = _build_cipher(key, iv)
        v = cipher.decrypt(data).rstrip()
        del cipher
        return v

    return decrypt

def encrypt(data):
    global key
    return encryptor(key)(data)

def decrypt(data):
    global key
    return decryptor(key)(data)
    