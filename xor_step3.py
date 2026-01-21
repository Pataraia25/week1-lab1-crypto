import base64


def xor_repeating(data: bytes, key: bytes) -> bytes:
    """XOR data with a repeating key."""
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))


# Assignment-given Base64 ciphertext
b64_ciphertext = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="

# Recovered passphrase from Task 2 (Step 2)
passphrase = "secure"

# Convert key to bytes
key_bytes = passphrase.encode("utf-8")

# Step 1: Base64 decode
cipher_bytes = base64.b64decode(b64_ciphertext)

# Step 2: XOR decrypt with repeating key
plaintext_bytes = xor_repeating(cipher_bytes, key_bytes)

print("Passphrase used:", passphrase)
print("Ciphertext (Base64):", b64_ciphertext)
print("\nDecrypted output:")

try:
    print(plaintext_bytes.decode("utf-8"))
except UnicodeDecodeError:
    print("Non-UTF8 output (hex):", plaintext_bytes.hex())
