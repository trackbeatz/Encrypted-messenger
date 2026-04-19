import os
import base64
import random  # New import for random colors
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

class Colors:
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'   # Added Blue
    WHITE = '\033[97m'  # Added White
    END = '\033[0m'
    BOLD = '\033[1m'

def display_logo():
    os.system("clear")
    
    # List of available colors
    logo_colors = [Colors.MAGENTA, Colors.CYAN, Colors.GREEN, Colors.YELLOW, Colors.RED, Colors.BLUE, Colors.WHITE]
    # Pick a random one
    random_color = random.choice(logo_colors)
    
    logo = r"""
    *****************************************
    * _________  ____  ___   ________ __   *
    * /_  __/ _ \/ _  |/ _ \ / ____/ //_/   *
    * / / / // / /_| / / / / /   / ,<      *
    * / / / _  / ___ / /_/ / /___/ /| |     *
    * /_/ /_/ |_/_/  |_\___\_\____/_/ |_|    *
    * *
    * SECURE Encrypted MESSENGER              *
    *****************************************
    """
    # Use the random_color variable here
    print(f"{random_color}{Colors.BOLD}{logo}{Colors.END}")
    print(f"{Colors.CYAN}System Active: {datetime.now().strftime('%Y-%m-%d %H:%M')}{Colors.END}")

# ... (rest of your functions: generate_keys, encrypt_msg, decrypt_msg, and main remain the same)

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    with open("my_private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    with open("my_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print(f"\n{Colors.GREEN}[+] Success! Keys saved in this folder.{Colors.END}")

def encrypt_msg(text, pub_key_path):
    with open(pub_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {text}"
    
    ciphertext = public_key.encrypt(
        full_message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()

def decrypt_msg(encrypted_base64):
    with open("my_private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    
    ciphertext = base64.b64decode(encrypted_base64)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

def main():
    display_logo()
    while True:
        print(f"\n{Colors.CYAN}{Colors.BOLD}--- Encrypted OPTIONS ---{Colors.END}")
        print(f"{Colors.YELLOW}1.{Colors.END} Setup (Generate My Keys)")
        print(f"{Colors.YELLOW}2.{Colors.END} Encrypt (Send a Message)")
        print(f"{Colors.YELLOW}3.{Colors.END} Decrypt (Read a Message)")
        print(f"{Colors.YELLOW}4.{Colors.END} Exit")
        
        choice = input(f"\n{Colors.MAGENTA}Select > {Colors.END}")

        if choice == "1":
            generate_keys()
        elif choice == "2":
            key_path = input("Enter filename of public key (e.g. my_public_key.pem): ")
            if os.path.exists(key_path):
                msg = input("Type your secret message: ")
                encrypted = encrypt_msg(msg, key_path)
                print(f"\n{Colors.GREEN}--- ENCRYPTED DATA ---{Colors.END}\n{encrypted}\n")
            else:
                print(f"{Colors.RED}Error: File '{key_path}' not found!{Colors.END}")
        elif choice == "3":
            blob = input("Paste the encrypted string: ")
            try:
                decrypted = decrypt_msg(blob)
                print(f"\n{Colors.GREEN}--- DECRYPTED MESSAGE ---{Colors.END}\n{decrypted}\n")
            except:
                print(f"{Colors.RED}Decryption failed! Wrong key or data error.{Colors.END}")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
