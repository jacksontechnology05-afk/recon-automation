import requests

url = input("Enter target URL (https://example.com): ")

vulnerabilities = {

    "Content-Security-Policy": {

        "name": "Missing Content Security Policy",

        "owasp": "A05 - Security Misconfiguration",

        "cvss": "6.5 (Medium)",

        "technical_risk":
        "May allow client-side script injection attacks.",

        "business_impact":
        "Could expose sensitive user data and weaken browser protections.",

        "recommendation":
        "Implement a strict Content-Security-Policy header.",

        "compliance":
        """
ISO 27001 A.8.28
NIST PR.DS-6
PCI-DSS Requirement 6.5
"""
    },

    "Strict-Transport-Security": {

        "name": "Missing Strict Transport Security",

        "owasp": "A02 - Cryptographic Failures",

        "cvss": "7.4 (High)",

        "technical_risk":
        "Traffic may be vulnerable to SSL stripping attacks.",

        "business_impact":
        "Sensitive communications could be intercepted by attackers.",

        "recommendation":
        "Enable HSTS with secure max-age configuration.",

        "compliance":
        """
ISO 27001 A.8.24
NIST PR.DS-2
PCI-DSS Requirement 4.1
"""
    }
}

try:

    response = requests.get(url, timeout=5)

    headers = response.headers

    print("\n===================================================")
    print(" SECURITY HEADERS VULNERABILITY ASSESSMENT")
    print("===================================================\n")

    for header, details in vulnerabilities.items():

        if header in headers:

            print(f"[+] {header} detected")

        else:

            print("---------------------------------------------------")

            print(f"Vulnerability:")
            print(f"{details['name']}\n")

            print("OWASP Category:")
            print(f"{details['owasp']}\n")

            print("CVSS Score:")
            print(f"{details['cvss']}\n")

            print("Technical Risk:")
            print(f"{details['technical_risk']}\n")

            print("Business Impact:")
            print(f"{details['business_impact']}\n")

            print("Recommendation:")
            print(f"{details['recommendation']}\n")

            print("Compliance Mapping:")
            print(f"{details['compliance']}")

            print("---------------------------------------------------\n")

except Exception as e:

    print(f"\n[-] Error: {e}")
