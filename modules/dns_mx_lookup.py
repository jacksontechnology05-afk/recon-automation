import dns.resolver

domain = input("Enter target domain: ")

print("\n===================================================")
print("           DNS / MX RECORD ANALYSIS")
print("===================================================\n")

try:

    mx_records = dns.resolver.resolve(domain, 'MX')

    print("[+] MX Records Found:\n")

    for mx in mx_records:
        print(mx.exchange)

except Exception as e:

    print(f"[-] MX Lookup Error: {e}")

print("\n===================================================")

try:

    txt_records = dns.resolver.resolve(domain, 'TXT')

    for record in txt_records:

        record_text = str(record)

        if "v=spf1" in record_text:

            print("\n[+] SPF Record Found:")
            print(record_text)

except:
    print("\n[-] SPF Record Not Found")
