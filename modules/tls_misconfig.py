import ssl
import socket

domain = input("Enter target domain: ")

print("\n===================================================")
print("        TLS MISCONFIGURATION SCANNER")
print("===================================================\n")

try:

    context = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:

        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            print("[+] TLS Connection Successful\n")

            print(f"TLS Version : {ssock.version()}")
            print(f"Cipher Used : {ssock.cipher()}")

            cert = ssock.getpeercert()

            print("\n[+] Certificate Subject:")
            print(cert.get('subject'))

            print("\n[+] Certificate Issuer:")
            print(cert.get('issuer'))

            # BASIC FINDINGS

            print("\n===================================================")
            print("                 SECURITY FINDINGS")
            print("===================================================\n")

            tls_version = ssock.version()

            if tls_version in ["TLSv1", "TLSv1.1"]:

                print("[!] Weak TLS Version Detected")
                print("Risk Level: HIGH")

            else:

                print("[+] Modern TLS Version Detected")

except Exception as e:

    print(f"\n[-] TLS Scan Failed: {e}")
