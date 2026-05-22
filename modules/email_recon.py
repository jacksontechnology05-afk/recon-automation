mport re
import socket

email = input("Enter target email: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):

    print("\n[+] Valid Email Format")

    domain = email.split("@")[1]

    print(f"[+] Domain: {domain}")

    try:

        ip = socket.gethostbyname(domain)

        print(f"[+] Resolved IP: {ip}")

    except:

        print("[-] Could not resolve domain")

else:

    print("[-] Invalid email format")
