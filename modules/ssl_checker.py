import ssl
import socket

hostname = input("Enter domain: ")

context = ssl.create_default_context()

try:

    with socket.create_connection((hostname, 443), timeout=5) as sock:

        with context.wrap_socket(sock, server_hostname=hostname) as ssock:

            cert = ssock.getpeercert()

            print("\n===================================================")
            print("            SSL CERTIFICATE CHECKER")
            print("===================================================\n")

            print(cert)

            print("\n===================================================")
            print("        SSL CERTIFICATE RETRIEVED")
            print("===================================================\n")

except Exception as e:

    print(f"\n[-] Error: {e}")
