def caesar_shift(text: str, shift: int) -> str:
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)


# Assignment-given ciphertext (Task 1)
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

print("Ciphertext:", ciphertext)
print("\nBruteforce results:")

# Brute-force all 26 shifts (decryption = negative shift)
for s in range(26):
    print(f"{s:2d}: {caesar_shift(ciphertext, -s)}")
