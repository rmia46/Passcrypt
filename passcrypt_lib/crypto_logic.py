# passcrypt_lib/crypto_logic.py
# Contains all core cryptographic operations.

import os
import json
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

# --- Constants ---
# These parameters are recommended by security standards.
SALT_SIZE = 16          # 128-bit salt for KDF
NONCE_SIZE = 12         # 96-bit nonce for AES-GCM (standard)
TAG_SIZE = 16           # 128-bit authentication tag for AES-GCM
KEY_SIZE = 32           # 256-bit key for AES
SCRYPT_N = 16384
SCRYPT_R = 8
SCRYPT_P = 1

backend = default_backend()

def derive_key(password: bytes, salt: bytes) -> bytes:
    """Derives a 256-bit key from a password and salt using Scrypt."""
    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P,
        backend=backend
    )
    return kdf.derive(password)

def encrypt_data(master_password: str, data_to_encrypt: dict) -> str:
    """
    Encrypts a dictionary of data using AES-256-GCM with a key derived
    from the master password.

    Returns:
        A single Base64 encoded string containing all necessary crypto parts.
    """
    try:
        password_bytes = master_password.encode('utf-8')
        plaintext = json.dumps(data_to_encrypt, indent=2).encode('utf-8')

        # 1. Generate random salt and nonce
        salt = os.urandom(SALT_SIZE)
        nonce = os.urandom(NONCE_SIZE)

        # 2. Derive a secure encryption key
        key = derive_key(password_bytes, salt)

        # 3. Encrypt the data
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)

        # 4. Bundle everything into a dictionary for storage
        encrypted_payload = {
            "kdf": "scrypt",
            "kdf_salt_b64": base64.b64encode(salt).decode('utf-8'),
            "cipher": "aes-256-gcm",
            "cipher_nonce_b64": base64.b64encode(nonce).decode('utf-8'),
            "ciphertext_b64": base64.b64encode(ciphertext).decode('utf-8'),
        }

        # 5. Encode the entire payload as a single Base64 string for easy storage
        payload_json = json.dumps(encrypted_payload)
        return base64.b64encode(payload_json.encode('utf-8')).decode('utf-8')

    except Exception as e:
        # Re-raise a more specific exception for the UI to catch
        raise ValueError(f"Encryption failed: {e}")


def decrypt_data(master_password: str, encrypted_blob: str) -> dict:
    """
    Decrypts a Base64 encoded blob using AES-256-GCM.

    Returns:
        The original dictionary of data if successful.
    
    Raises:
        ValueError: If decryption fails due to incorrect password, tampering, or format.
    """
    try:
        # 1. Decode the outer Base64 layer to get the JSON payload
        payload_json = base64.b64decode(encrypted_blob).decode('utf-8')
        encrypted_payload = json.loads(payload_json)

        # 2. Extract and decode all the necessary crypto parts
        salt = base64.b64decode(encrypted_payload["kdf_salt_b64"])
        nonce = base64.b64decode(encrypted_payload["cipher_nonce_b64"])
        ciphertext = base64.b64decode(encrypted_payload["ciphertext_b64"])
        
        password_bytes = master_password.encode('utf-8')

        # 3. Re-derive the same key using the provided salt
        key = derive_key(password_bytes, salt)

        # 4. Decrypt and authenticate the data
        aesgcm = AESGCM(key)
        decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)

        # 5. Decode the plaintext and return the original dictionary
        decrypted_data = json.loads(decrypted_bytes.decode('utf-8'))
        return decrypted_data

    except Exception as e:
        # The most common failure is an incorrect password, which leads to a
        # `cryptography.exceptions.InvalidTag` error. We catch all exceptions
        # to be safe and return a generic, user-friendly error message.
        raise ValueError("Decryption failed. Check your master key or the encrypted data.")
