import socket

domain = input("Enter domain: ")

subdomains = ["www", "mail", "ftp", "admin", "test", "dev"]

print(f"\n[+] Enumerating subdomains for {domain}\n")

for sub in subdomains:

    subdomain = f"{sub}.{domain}"

    try:

        ip = socket.gethostbyname(subdomain)

        print(f"[+] Found: {subdomain} --> {ip}")

    except:

        pass
