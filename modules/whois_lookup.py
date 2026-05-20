import whois
import json

domain = input("Enter domain: ")

try:

    info = whois.whois(domain)

    print("\n[+] WHOIS Information:\n")

    print(json.dumps(info, indent=4, default=str))

except Exception as e:

    print(f"\n[-] Error: {e}")
