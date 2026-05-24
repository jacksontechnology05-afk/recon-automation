import requests

url = input("Enter target URL (https://example.com): ")

print("\n===================================================")
print("            CVE FINGERPRINTING")
print("===================================================\n")

try:

    response = requests.get(url, timeout=5)

    headers = response.headers

    server = headers.get("Server")

    powered = headers.get("X-Powered-By")

    if server:
        print(f"[+] Server Detected: {server}")

    if powered:
        print(f"[+] Technology Detected: {powered}")

    print("\n===================================================")
    print("          POTENTIAL TECHNOLOGY RISKS")
    print("===================================================\n")

    if server:

        if "Apache" in server:
            print("[!] Apache Detected")
            print("Potential CVEs may exist depending on version.")

        elif "nginx" in server.lower():
            print("[!] Nginx Detected")
            print("Validate against latest nginx CVEs.")

    if powered:

        if "PHP" in powered:
            print("[!] PHP Detected")
            print("Check for outdated PHP vulnerabilities.")

        elif "ASP.NET" in powered:
            print("[!] ASP.NET Detected")
            print("Validate framework patch level.")

except Exception as e:

    print(f"\n[-] Fingerprinting Failed: {e}")
