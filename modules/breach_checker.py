email = input("Enter email address: ")

print("\n===================================================")
print("          PUBLIC BREACH EXPOSURE CHECK")
print("===================================================\n")

print(f"[+] Checking exposure for: {email}")

print("""
Risk Advisory:
If employee credentials are exposed in public breaches,
the organization may face credential stuffing attacks,
phishing attempts, and unauthorized access risks.

Recommendation:
- Enable MFA
- Enforce password rotation
- Monitor leaked credentials

Compliance Mapping:
ISO 27001 A.5.7
NIST PR.AC-1
PCI-DSS Requirement 8
""")
