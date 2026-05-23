domain = input("Enter target domain: ")

print("\n===================================================")
print("      EMPLOYEE EMAIL PATTERN DISCOVERY")
print("===================================================\n")

patterns = [
    f"firstname.lastname@{domain}",
    f"firstname@{domain}",
    f"flastname@{domain}",
    f"lastname.firstname@{domain}"
]

print("[+] Common Corporate Email Patterns:\n")

for pattern in patterns:
    print(pattern)

print("""
Business Impact:
Predictable email naming conventions may assist
phishing and social engineering attacks.

Recommendation:
Implement security awareness training and MFA.
""")
