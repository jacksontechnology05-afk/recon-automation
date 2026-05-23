import dns.resolver

domain = input("Enter target domain: ")

print("\n===================================================")
print("           SPF / DMARC VALIDATOR")
print("===================================================\n")

# SPF CHECK

try:

    txt_records = dns.resolver.resolve(domain, 'TXT')

    spf_found = False

    for record in txt_records:

        if "v=spf1" in str(record):

            spf_found = True

            print("[+] SPF Record Found:")
            print(record)

    if not spf_found:
        print("[-] SPF Record Missing")

except:
    print("[-] SPF Check Failed")

# DMARC CHECK

try:

    dmarc = "_dmarc." + domain

    dmarc_records = dns.resolver.resolve(dmarc, 'TXT')

    print("\n[+] DMARC Record Found:")

    for record in dmarc_records:
        print(record)

except:
    print("\n[-] DMARC Record Missing")
