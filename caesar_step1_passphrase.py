def caesar_shift_lower(text: str, shift: int) -> str:
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            out.append(ch)
    return "".join(out)


# Assignment-given ciphertext
ciphertext = "mznxpz"

print("Ciphertext:", ciphertext)
print("\nBruteforce results:")

# Brute-force all 26 shifts (decryption = negative shift)
for s in range(26):
    print(f"{s:2d}: {caesar_shift_lower(ciphertext, -s)}")
