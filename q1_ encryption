def encrypt(text, shift):
    """Encrypt text using Caesar Cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    """Decrypt text using Caesar Cipher"""
    return encrypt(text, -shift)


# === Main Program ===
shift = int(input("Enter shift number for encryption/decryption: "))

# Step 1: Read original text
with open("input.txt", "r") as f:
    original_text = f.read()

# Step 2: Encrypt and save
encrypted_text = encrypt(original_text, shift)
with open("encrypted.txt", "w") as f:
    f.write(encrypted_text)
print("✅ File encrypted → saved as encrypted.txt")

# Step 3: Decrypt and save
decrypted_text = decrypt(encrypted_text, shift)
with open("decrypted.txt", "w") as f:
    f.write(decrypted_text)
print("✅ File decrypted → saved as decrypted.txt")

# Step 4: Compare decrypted with original
if original_text == decrypted_text:
    print("🎉 Success! Decrypted text matches the original.")
else:
    print("⚠️ Error: Decrypted text does NOT match the original.")
