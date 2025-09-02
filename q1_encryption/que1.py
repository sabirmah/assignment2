def encrypt_char(c, shift1, shift2):
    if c.islower():
        if 'a' <= c <= 'm':
            return chr((ord(c) - ord('a') + shift1 * shift2) % 26 + ord('a'))
        elif 'n' <= c <= 'z':
            return chr((ord(c) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
    elif c.isupper():
        if 'A' <= c <= 'M':
            return chr((ord(c) - ord('A') - shift1) % 26 + ord('A'))
        elif 'N' <= c <= 'Z':
            return chr((ord(c) - ord('A') + shift2**2) % 26 + ord('A'))
    else:
        return c

def decrypt_char(c, shift1, shift2):
    if c.islower():
        if 'a' <= c <= 'm':
            return chr((ord(c) - ord('a') - shift1 * shift2) % 26 + ord('a'))
        elif 'n' <= c <= 'z':
            return chr((ord(c) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
    elif c.isupper():
        if 'A' <= c <= 'M':
            return chr((ord(c) - ord('A') + shift1) % 26 + ord('A'))
        elif 'N' <= c <= 'Z':
            return chr((ord(c) - ord('A') - shift2**2) % 26 + ord('A'))
    else:
        return c

def encrypt_file(input_file, output_file, shift1, shift2):
    with open(input_file, 'r') as f:
        text = f.read()
    encrypted_text = ''.join(encrypt_char(c, shift1, shift2) for c in text)
    with open(output_file, 'w') as f:
        f.write(encrypted_text)

def decrypt_file(input_file, output_file, shift1, shift2):
    with open(input_file, 'r') as f:
        text = f.read()
    decrypted_text = ''.join(decrypt_char(c, shift1, shift2) for c in text)
    with open(output_file, 'w') as f:
        f.write(decrypted_text)

def verify_decryption(original_file, decrypted_file):
    with open(original_file, 'r') as f1, open(decrypted_file, 'r') as f2:
        if f1.read() == f2.read():
            print("Decryption successful!")
        else:
            print("Decryption failed!")

# Main program
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypt_file('raw_text.txt', 'encrypted_text.txt', shift1, shift2)
decrypt_file('encrypted_text.txt', 'decrypted_text.txt', shift1, shift2)
verify_decryption('raw_text.txt', 'decrypted_text.txt')
