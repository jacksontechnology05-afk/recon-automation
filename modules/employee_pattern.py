import socket

domain = input("Enter target domain: ")

print("\n===================================================")
print("      EMPLOYEE EMAIL INTELLIGENCE")
print("===================================================\n")

# Common corporate naming conventions

patterns = [
    f"firstname.lastname@{domain}",
    f"firstname@{domain}",
    f"flastname@{domain}",
    f"lastname.firstname@{domain}",
    f"admin@{domain}",
    f"support@{domain}",
    f"hr@{domain}",
    f"it@{domain}",
    f"security@{domain}"
]

print("[+] Potential Corporate Email Patterns:\n")

for pattern in patterns:
    print(f" - {pattern}")

print("\n===================================================")

# DNS Resolution

try:

    ip = socket.gethostbyname(domain)

    print(f"[+] Domain Resolved Successfully: {ip}")

except Exception as e:

    print(f"[-] DNS Resolution Failed: {e}")

print("\n===================================================")

# Risk Assessment

print("""
Risk Assessment:
Publicly exposed corporate email structures may assist:

- Phishing campaigns
- Social engineering attacks
- Credential stuffing
- Business Email Compromise (BEC)

Business Impact:
Attackers may impersonate employees or target staff
with malicious payloads and credential theft attempts.

Security Recommendation:
- Enforce Multi-Factor Authentication (MFA)
- Deploy Email Security Gateway
- Conduct Security Awareness Training
- Implement SPF, DKIM, and DMARC

Compliance Mapping:
ISO 27001 A.5.7
NIST PR.AC-1
PCI-DSS Requirement 8
""")
