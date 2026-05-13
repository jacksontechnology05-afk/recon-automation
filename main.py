import socket

print("🔐 Recon Automation Toolkit")

target = input("Enter target domain or IP: ")

try:
    ip = socket.gethostbyname(target)
    print(f"[+] IP Address: {ip}")
except socket.gaierror:
    print("[-] Unable to resolve target.")
