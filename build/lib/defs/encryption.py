from cryptography.fernet import Fernet


def encrypt(string: str) -> tuple[bytes, bytes]:
    """
    It takes a string,
    encrypts it,
    and returns the encrypted string and the key used to encrypt it

    Parameters
    ----------
    string : str
        str

    Returns
    -------
        A tuple of two bytes objects.

    """
    key: bytes = Fernet.generate_key()
    return Fernet(key).encrypt(string.encode()), key


def encrypt_with_existing_key(string: str, key: bytes):
    """
    It takes a string and a key,
    and returns the encrypted version of the string

    Parameters
    ----------
    string : str
        The string you want to encrypt
    key : bytes
        bytes

    Returns
    -------
        A byte string

    """
    return Fernet(key).encrypt(string.encode())


def decrypt(string: bytes, key: bytes) -> str:
    """
    It takes a string and a key,
    and returns the decrypted string

    Parameters
    ----------
    string : bytes
        The string to be decrypted.
    key : bytes
        The key used to encrypt and decrypt the string.

    Returns
    -------
        The decrypted string.

    """
    return Fernet(key).decrypt(string).decode()
