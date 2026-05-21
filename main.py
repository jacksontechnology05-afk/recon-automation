
while True:

    os.system("clear")

    print("""
============================================================
             JACKSON RECON AUTOMATION TOOLKIT
============================================================

Author : Jackson Nnkemdilim Godwin
Role   : Cybersecurity Analyst & Penetration Tester

"With great power comes great responsibility."

This toolkit is intended strictly for:
- Educational Purposes
- Authorized Security Assessments
- Ethical Penetration Testing
- Security Research

Unauthorized usage against systems without proper
authorization is strictly prohibited.

============================================================
                    AVAILABLE MODULES
============================================================

1. Port Scanner
2. Banner Grabber
3. WHOIS Lookup
4. HTTP Headers Analyzer
5. SSL Checker
6. Subdomain Enumeration
7. Security Headers Vulnerability Scanner
8. Exit Toolkit

============================================================
""")

    choice = input("Select option: ")

    if choice == "1":
        exec(open("modules/port_scanner.py").read())

    elif choice == "2":
        exec(open("modules/banner_grabber.py").read())

    elif choice == "3":
        exec(open("modules/whois_lookup.py").read())

    elif choice == "4":
        exec(open("modules/http_headers.py").read())

    elif choice == "5":
        exec(open("modules/ssl_checker.py").read())

    elif choice == "6":
        exec(open("modules/subdomain_enum.py").read())

    elif choice == "7":
        exec(open("modules/security_headers_scanner.py").read())

    elif choice == "8":
        print("\n[+] Exiting Toolkit...")
        break

    else:
        print("\n[-] Invalid option.")

    input("\nPress ENTER to continue...")
