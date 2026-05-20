import socket

target = input("Enter target IP or domain: ")
port = int(input("Enter port: "))

try:

    s = socket.socket()

    s.settimeout(3)

    s.connect((target, port))

    banner = s.recv(1024)

    print(f"\n[+] Banner: {banner.decode().strip()}")

    s.close()

except Exception as e:

    print(f"\n[-] Error: {e}")
