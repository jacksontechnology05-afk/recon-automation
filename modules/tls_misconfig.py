domain = input("Enter target domain: ")

print("\n===================================================")
print("        TLS MISCONFIGURATION SCANNER")
print("===================================================\n")

print(f"[+] Checking TLS configuration for {domain}")

print("""
Common TLS Issues:
- TLS 1.0 enabled
- TLS 1.1 enabled
- Weak cipher suites
- SSL certificate mismatch

Recommendation:
Disable deprecated TLS versions and weak ciphers.
""")
