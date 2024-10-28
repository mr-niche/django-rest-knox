import binascii
from os import urandom as generate_bytes

from knox.settings import knox_settings

hash_func = knox_settings.SECURE_HASH_ALGORITHM


def create_token_string() -> str:
    return binascii.hexlify(
        generate_bytes(int(knox_settings.AUTH_TOKEN_CHARACTER_LENGTH / 2))
    ).decode()


def make_hex_compatible(token: str) -> bytes:
    """
    Ensure a token, which may contain a TOKEN_PREFIX, is hex-compatible before hashing.
    """
    try:
        # use the original method for hashing a token pre v5.0.*
        # this ensure tokens generated in v4.2 will remain valid in v5.1+
        return binascii.unhexlify(token)
    except (binascii.Error, ValueError):
        # if a token has a prefix, encode it so that it's hex-compatible and can be hashed
        return binascii.hexlify(token.encode('utf-8'))


def hash_token(token: str) -> str:
    """
    Calculates the hash of a token.
    Token must contain an even number of hex digits or
    a binascii.Error exception will be raised.
    """
    digest = hash_func()
    digest.update(make_hex_compatible(token))
    return digest.hexdigest()
