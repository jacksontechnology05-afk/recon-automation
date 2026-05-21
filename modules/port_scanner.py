import socket

target = input("Enter target IP or domain: ")

ports = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]

try:

    ip = socket.gethostbyname(target)

    print(f"\n[+] Resolved IP: {ip}")
    print(f"[+] Scanning {target}...\n")

    for port in ports:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

        s.close()

except socket.gaierror:

    print("\n[-] Invalid domain or host unreachable.")
