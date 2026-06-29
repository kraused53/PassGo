import base64
import json
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

_SALT_SIZE = 16
_KDF_ITERATIONS = 480000

def _derive_key(user_password: str, salt: bytes) -> Fernet | None:
    """
    Generate a Fernet encryption system using the user's password

    :param user_password: The plaintext user password
    :param salt: The generated salt (used to obscure user's password in .dat file)
    :return: On success: return Fernet encryption class. On failure: return None
    """
    if not user_password:
        print("_derive_key: user_password cannot be empty!")
        return None

    if not salt:
        print("_derive_key: salt cannot be empty!")
        return None

    if len(salt) != _SALT_SIZE:
        print("_derive_key: invalid salt length!")  
        return None

    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=_KDF_ITERATIONS,
        )
        key = base64.urlsafe_b64encode(kdf.derive(user_password.encode()))
        return Fernet(key)
    except ValueError as e:
        print(f"_derive_key: key generation error! {e}")
        return None
    except Exception as e:
        print(f"_derive_key: unknown error! {e}")
        return None

def encrypt_dictionary(user_password: str, to_encrypt: dict) -> bytes | None:
    """
    Take a plaintext password and a dictionary. Encrypt the dictionary using the password and return it as a bytes object

    :param user_password: Plaintext user password
    :param to_encrypt: The dictionary to encrypt
    :return: On success: return encrypted dictionary. On failure: return None
    """
    if not user_password:
        print("encrypt_dictionary: user_password cannot be empty!")
        return None

    if not to_encrypt:
        print("encrypt_dictionary: to_encrypt cannot be empty!")
        #return None

    # convert dict into JSON for serialization
    try:
        to_encrypt = json.dumps(to_encrypt)
    except TypeError:
        print("encrypt_dictionary: to_encrypt must be a dict!")
        return None

    # Generate key and encrypt
    try:
        salt = os.urandom(_SALT_SIZE)
        fernet = _derive_key(user_password, salt)
        token = fernet.encrypt(to_encrypt.encode())
        return salt + token
    except Exception as e:
        print(f"encrypt_dictionary: error encrypting {e}")
        return None

def decrypt_dictionary(password: str, to_decrypt: bytes) -> dict | None:
    """
    Take a bytes object and a user password. Attempt to decrypt the bytes object into  a dictionary using the given password

    :param password: Plaintext user password
    :param to_decrypt: Bytes object to decrypt
    :return: On success: return decrypted dictionary. On failure: return None
    """
    # Split salt from data
    salt, token = to_decrypt[:_SALT_SIZE], to_decrypt[_SALT_SIZE:]

    # Generate the key given the salt and the password
    fernet = _derive_key(password, salt)
    if not fernet:
        return None

    try:
        data = fernet.decrypt(token).decode()
        return json.loads(data)
    except InvalidToken:
        print('decrypt_dictionary: invalid password or corrupted file!')
        return None
    except Exception as e:
        print(f"decrypt_dictionary: error decrypting {e}")
        return None



if __name__ == "__main__":
    password_record = {
        "google": "password",
        "IRS": "password123",
        "Bank": "passwordABC",
        "Nuclear Codes": "1234"
    }
    ciphertext = encrypt_dictionary("password", password_record)
    print(ciphertext)
    plaintext = decrypt_dictionary("password", ciphertext)
    print(plaintext)
    print(plaintext['Nuclear Codes'])
