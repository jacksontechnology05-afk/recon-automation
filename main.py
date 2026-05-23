import os

while True:

    os.system("clear")

    print("""
============================================================
         JACKSON SECURITY ASSESSMENT FRAMEWORK
============================================================

Author : Jackson Nnkemdilim Godwin
Role   : Cybersecurity Analyst & Penetration Tester

"Think no evil. Do no evil."

This framework is intended strictly for:
- Educational Purposes
- Authorized Security Assessments
- Ethical Penetration Testing
- Security Research

Unauthorized usage against systems without proper
authorization is strictly prohibited.

============================================================
        RECON • OSINT • EXPOSURE • VALIDATION
============================================================

[ RECONNAISSANCE ]

1. Port Scanner
2. Banner Grabber
3. WHOIS Lookup
4. HTTP Headers Analyzer
5. SSL Checker
6. Subdomain Enumeration

[ OSINT & EXPOSURE ]

7. Email & OSINT Recon
8. DNS / MX Record Lookup
9. Public Breach Checker
10. Employee Email Pattern Discovery
11. SPF / DMARC Validator

[ VULNERABILITY VALIDATION ]

12. Security Headers Scanner
13. OWASP Top 10 Validator
14. TLS Misconfiguration Scanner
15. CVE Fingerprinting

[ REPORTING & COMPLIANCE ]

16. Compliance Mapper

[ EXIT ]

17. Exit Framework

============================================================
""")

    choice = input("Select option: ")

    # RECONNAISSANCE

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

    # OSINT & EXPOSURE

    elif choice == "7":
        exec(open("modules/email_osint.py").read())

    elif choice == "8":
        exec(open("modules/dns_mx_lookup.py").read())

    elif choice == "9":
        exec(open("modules/breach_checker.py").read())

    elif choice == "10":
        exec(open("modules/employee_pattern.py").read())

    elif choice == "11":
        exec(open("modules/spf_dmarc_validator.py").read())

    # VULNERABILITY VALIDATION

    elif choice == "12":
        exec(open("modules/security_headers_scanner.py").read())

    elif choice == "13":
        exec(open("modules/owasp_validator.py").read())

    elif choice == "14":
        exec(open("modules/tls_misconfig.py").read())

    elif choice == "15":
        exec(open("modules/cve_fingerprint.py").read())

    # REPORTING & COMPLIANCE

    elif choice == "16":
        exec(open("modules/compliance_mapper.py").read())

    # EXIT

    elif choice == "17":
        print("\n[+] Exiting Framework...")
        break

    else:
        print("\n[-] Invalid option.")

    input("\nPress ENTER to continue...")
