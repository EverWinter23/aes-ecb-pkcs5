"""
30th august 2022 tuesday
out of the old, into the new
"""

import hashlib
from base64 import b64decode as b64D
from base64 import b64encode as b64E

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

UTF_8 = "utf-8"


def make_aes_ecb_cipher(secret: str, key_size: int = 16) -> Cipher:
    """Makes the AES/ECB cipher using python stdlib packages.

    Args:
        secret (str): Shared secret
        key_size (int): Size of the key made using the secret

    Returns:
        Cipher: Returns the AES/ECB cipher for encryption/decryption
    """
    return Cipher(
        algorithms.AES(make_key(secret, key_size)),
        modes.ECB(),
        backend=default_backend(),
    )


def make_key(secret: str, key_size: int) -> str:
    """Create the key used for AES encryption/decryption using
    the shared secret.

    Args:
        secret (str): Shared secret
        key_size (int): Size of the key made using the secret

    Returns:
        str: Key used for AES encryption/decryption
    """
    if key_size <= 0:
        AssertionError("key_size cannot be <=0.")
    return hashlib.sha256(secret.encode(UTF_8)).digest()[:key_size]


def encrypt_to_base64(plain_text: str, secret: str, key_size: int) -> str:
    """Encrypts plain_text to AES/ECB/PKCS5 encrypted text.

    Args:
        plain_text (str): Text which will be encrypted to aes_ecb_pkcs5 b64
        secret (str): Shared secret
        key_size (int): Size of the key made using the secret

    Returns:
        str: Encrypted text using AES/ECB/PKCS5 encryption in base64
    """
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_bytes = padder.update(plain_text.encode(UTF_8)) + padder.finalize()
    cipher = make_aes_ecb_cipher(secret, key_size)
    encryptor = cipher.encryptor()
    encrypted_bytes = encryptor.update(padded_bytes) + encryptor.finalize()
    return b64E(encrypted_bytes).decode(UTF_8)


def decrypt_from_base64(encrypted_text: str, secret: str, key_size: int) -> str:
    """Decrypts base64 encoded encrypted text using AES/ECB/PKCS5 to plain text.

    Args:
        encrypted_text (str): Base64 encoded encrypted text
        secret (str): Shared secret
        key_size (int): Size of the key made using the secret

    Returns:
        str: Encrypted text using AES/ECB/PKCS5 encryption in base64
    """
    encrypted_bytes = b64D(encrypted_text)
    cipher = make_aes_ecb_cipher(secret, key_size)
    decryptor = cipher.decryptor()
    padded_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_bytes = unpadder.update(padded_bytes) + unpadder.finalize()
    return unpadded_bytes.decode(UTF_8)
