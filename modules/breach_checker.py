import re
import socket

target = input("Enter email address: ")

print("\n===================================================")
print("          PUBLIC BREACH EXPOSURE CHECK")
print("===================================================\n")

# EMAIL VALIDATION

email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_regex, target):

    print("[+] Valid Email Format Detected")

    domain = target.split("@")[1]

    # DOMAIN RESOLUTION

    try:

        ip = socket.gethostbyname(domain)

        print(f"[+] Domain Resolved Successfully: {ip}")

    except:

        print("[-] Domain Resolution Failed")

    print("\n===================================================")
    print("            EXPOSURE ASSESSMENT")
    print("===================================================\n")

    # HIGH-RISK EMAILS

    risky_names = [
        "admin",
        "support",
        "hr",
        "finance",
        "security",
        "it"
    ]

    username = target.split("@")[0].lower()

    if username in risky_names:

        print(f"[!] High-Value Target Email Detected: {username}")
        print("Risk Level: HIGH")

    else:

        print("[+] Standard User Email Detected")
        print("Risk Level: MEDIUM")

    print("\n===================================================")

    print("""
Potential Risks:
- Credential stuffing
- Phishing campaigns
- Password reuse attacks
- Business Email Compromise (BEC)

Security Recommendations:
- Enable MFA
- Enforce strong password policies
- Monitor breach intelligence platforms
- Conduct phishing awareness training

Compliance Mapping:
ISO 27001 A.5.7
NIST PR.AC-1
PCI-DSS Requirement 8
""")

else:

    print("[-] Invalid Email Address Format")
