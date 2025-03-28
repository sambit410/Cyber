import hashlib
import socket
import sys

# Function 1: File Hash Checker
def check_file_hash(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()
            md5_hash = hashlib.md5(data).hexdigest()
            print(f"MD5 Hash of {filename}: {md5_hash}")
            return md5_hash
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None

# Function 2: Port Scanner
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Quick timeout to avoid hanging
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN on {ip}")
    else:
        print(f"Port {port} is CLOSED on {ip}")
    sock.close()

# Main Menu for the Toolkit
def main():
    print("=== Sambit’s Cybersecurity Toolkit ===")
    print("1. Check File Hash")
    print("2. Scan a Port")
    print("3. Exit")
    
    while True:
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            filename = input("Enter filename to hash (e.g., test.txt): ")
            check_file_hash(filename)
        
        elif choice == "2":
            ip = input("Enter IP to scan (e.g., 127.0.0.1): ")
            try:
                port = int(input("Enter port to scan (e.g., 80): "))
                scan_port(ip, port)
            except ValueError:
                print("Error: Port must be a number!")
        
        elif choice == "3":
            print("Exiting toolkit. Good luck!")
            sys.exit()
        
        else:
            print("Invalid choice! Pick 1, 2, or 3.")

# Run the toolkit
if __name__ == "__main__":
    main()
