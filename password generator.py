import random
import string

#encryption method
def xor_encrypt(text, key="mysecretkey"):
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    return encrypted

def xor_decrypt(encrypted_text, key="mysecretkey"):
    decrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted_text))
    return decrypted

#generates random passwords
def generate_password():
    character_pool = string.ascii_letters + string.digits
    password = ''.join(random.choices(character_pool, k=8))
    return password

#saves passwords
def save_password(site, password):
    encrypted_pw = xor_encrypt(password)
    with open('passwords.txt', 'a') as file:
        file.write(f"{site}: {encrypted_pw}\n")
        
#reads passwords and decrypts them
def read_passwords():
    try:
        with open('passwords.txt', 'r') as file:
            print("\n=== Saved Passwords ===")
            for line in file:
                if ": " in line:
                    site, encrypted = line.strip().split(": ")
                    decrypted = xor_decrypt(encrypted)
                    print(f"{site}: {decrypted}")
    except FileNotFoundError:
        print("No saved passwords found.")

#logic for the main menu
def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Generate new password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            site = input("Enter the website or app name: ")
            password = generate_password()
            print(f"Generated password: {password}")
            save_password(site, password)
            print("Password saved.")
        elif choice == "2":
            read_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

main()
