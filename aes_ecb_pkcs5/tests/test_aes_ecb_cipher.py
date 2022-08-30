from aes_ecb_pkcs5 import encrypt_to_base64, decrypt_from_base64


SHARED_ENCODING_KEY = "rFIRwsZguXoBCgUIZZptLsRMJ"
PLAIN_TEXT = "eternal.blizzard23@gmail.com"
ENCRYPTED_TEXT = "Oa2+V0o50rtq8O6higMZ9DEHg5AOf7K4QuHKZ3zTwVk=" 

def test_encryption():
    assert encrypt_to_base64(PLAIN_TEXT, SHARED_ENCODING_KEY, 16) == ENCRYPTED_TEXT 


def test_decryption():
    assert decrypt_from_base64(ENCRYPTED_TEXT, SHARED_ENCODING_KEY, 16) == PLAIN_TEXT

