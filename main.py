 
import dns.resolver

domain = input("Enter target domain: ")

print("\n===================================================")
print("        EMAIL & OSINT RECONNAISSANCE")
print("===================================================\n")

# Common email patterns

emails = [
    f"admin@{domain}",
    f"support@{domain}",
    f"info@{domain}",
    f"hr@{domain}",
    f"contact@{domain}"
]

print("[+] Common Email Addresses Found:\n")

for email in emails:
    print(email)

print("\n===================================================")

# MX RECORD LOOKUP

try:

    mx_records = dns.resolver.resolve(domain, 'MX')

    print("\n[+] MX Records:\n")

    for mx in mx_records:
        print(mx.exchange)

except Exception as e:

    print(f"\n[-] MX Lookup Error: {e}")

print("\n===================================================")

# SPF CHECK

try:

    txt_records = dns.resolver.resolve(domain, 'TXT')

    spf_found = False

    for record in txt_records:

        record_text = str(record)

        if "v=spf1" in record_text:

            spf_found = True

            print("\n[+] SPF Record Detected:")
            print(record_text)

    if not spf_found:

        print("\n[-] No SPF Record Found")

except Exception as e:

    print(f"\n[-] SPF Check Error: {e}")

print("\n===================================================")

# BUSINESS RISK

print("""
Business Risk:
Exposed company email addresses may increase
phishing and credential attack exposure.

Recommendation:
Implement MFA, SPF, DKIM, and DMARC protections.

Compliance Mapping:
ISO 27001 A.5.7
NIST PR.AC-1
PCI-DSS Requirement 8
""")
