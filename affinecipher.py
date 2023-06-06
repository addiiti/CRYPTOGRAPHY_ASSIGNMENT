def encrypt(plaintext, a, b):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, a, b):
    decrypted_text = ''
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((a_inverse * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                decrypted_char = chr((a_inverse * (ord(char) - ord('a') - b)) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

# Example usage
def run_affine_cipher():
    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\n")
        
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            a = int(input("Enter the multiplicative key (a): "))
            b = int(input("Enter the additive key (b): "))
            encrypted_text = encrypt(plaintext, a, b)
            print("Encrypted text:", encrypted_text)
        
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            a = int(input("Enter the multiplicative key (a): "))
            b = int(input("Enter the additive key (b): "))
            decrypted_text = decrypt(ciphertext, a, b)
            print("Decrypted text:", decrypted_text)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

run_affine_cipher()
