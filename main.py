#!/usr/bin/env python3
import socket
import requests
import whois
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    print("""
    ┌─────────────────────────────────────────────────────────────┐
    │           JACKSON RECON AUTOMATION TOOLKIT                  │
    ├─────────────────────────────────────────────────────────────┤
    │  Author : Jackson Nnkemdilim Godwin                        │
    │  Role   : Cybersecurity Analyst & Penetration Tester       │
    │                                                             │
    │  "With great power comes great responsibility."            │
    ├─────────────────────────────────────────────────────────────┤
    │  This toolkit is intended strictly for:                    │
    │  - Educational Purposes                                    │
    │  - Authorized Security Assessments                         │
    │  - Ethical Penetration Testing                             │
    │  - Security Research                                       │
    └─────────────────────────────────────────────────────────────┘
    """)

def port_scanner(target):
    """Port Scanner Module"""
    print(f"\n[+] Scanning ports on {target}")
    ports = [20,21,22,23,25,53,80,110,135,139,143,443,445,3306,3389,8080]
    open_ports = []
    
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Target IP: {ip}\n")
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"    ✅ Port {port}: OPEN")
                    open_ports.append(port)
                else:
                    print(f"    ❌ Port {port}: CLOSED")
                sock.close()
            except Exception as e:
                print(f"    ⚠️ Port {port}: Error - {e}")
        
        if open_ports:
            print(f"\n[+] Open ports found: {open_ports}")
        else:
            print("\n[-] No open ports found")
            
    except Exception as e:
        print(f"[-] Error: {e}")

def banner_grabber(target, port):
    """Banner Grabber Module"""
    print(f"\n[+] Grabbing banner from {target}:{port}")
    
    try:
        ip = socket.gethostbyname(target)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, int(port)))
        
        # Send a generic probe
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
        
        # Receive banner
        banner = sock.recv(1024)
        print(f"\n[+] Banner received:\n")
        print(banner.decode('utf-8', errors='ignore'))
        sock.close()
        
    except ConnectionRefusedError:
        print(f"[-] Connection refused on port {port}")
        print("[!] Port may be closed or firewalled")
    except socket.timeout:
        print(f"[-] Connection timeout on port {port}")
    except Exception as e:
        print(f"[-] Error: {e}")

def whois_lookup(target):
    """WHOIS Lookup Module"""
    print(f"\n[+] WHOIS Lookup for {target}")
    try:
        w = whois.whois(target)
        if w.registrar:
            print(f"    Registrar: {w.registrar}")
        if w.creation_date:
            print(f"    Created: {w.creation_date}")
        if w.expiration_date:
            print(f"    Expires: {w.expiration_date}")
        if w.name_servers:
            print(f"    Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"    [-] WHOIS Error: {e}")

def http_headers(target):
    """HTTP Headers Analyzer"""
    print(f"\n[+] HTTP Headers for https://{target}")
    try:
        r = requests.get(f"https://{target}", timeout=10, verify=False)
        print("\n    RESPONSE HEADERS:\n")
        for header, value in r.headers.items():
            print(f"    {header}: {value}")
    except requests.exceptions.ConnectionError:
        print(f"[-] Failed to connect to https://{target}")
        print("[!] Trying http://...")
        try:
            r = requests.get(f"http://{target}", timeout=10)
            for header, value in r.headers.items():
                print(f"    {header}: {value}")
        except Exception as e:
            print(f"[-] HTTP Error: {e}")
    except Exception as e:
        print(f"[-] HTTP Error: {e}")

def ssl_checker(target):
    """SSL Certificate Checker"""
    print(f"\n[+] SSL Checker for {target}")
    print("    [Coming soon in next update]")
    # TODO: Add SSL checking with ssl module

def subdomain_enum(target):
    """Subdomain Enumeration"""
    print(f"\n[+] Subdomain Enumeration for {target}")
    print("    [Coming soon in next update]")
    # TODO: Add subdomain enumeration

def security_headers_scanner(target):
    """Security Headers Vulnerability Scanner"""
    print(f"\n[+] Security Headers Scan for https://{target}")
    try:
        r = requests.get(f"https://{target}", timeout=10, verify=False)
        
        checks = {
            'Content-Security-Policy': 'HIGH',
            'Strict-Transport-Security': 'HIGH',
            'X-Frame-Options': 'MEDIUM',
            'X-Content-Type-Options': 'LOW',
            'Referrer-Policy': 'LOW',
            'Permissions-Policy': 'LOW'
        }
        
        print("\n    SECURITY HEADERS ANALYSIS:\n")
        for header, severity in checks.items():
            if header in r.headers:
                print(f"    ✅ {header}: Present ({severity})")
                print(f"       Value: {r.headers[header][:80]}")
            else:
                print(f"    ❌ {header}: MISSING ({severity})")
                
    except Exception as e:
        print(f"[-] Scan Error: {e}")

def main():
    while True:
        clear_screen()
        show_banner()
        
        print("\n    AVAILABLE MODULES\n")
        print("    1. Port Scanner")
        print("    2. Banner Grabber")
        print("    3. WHOIS Lookup")
        print("    4. HTTP Headers Analyzer")
        print("    5. SSL Checker")
        print("    6. Subdomain Enumeration")
        print("    7. Security Headers Vulnerability Scanner")
        print("    8. Exit Toolkit")
        print("\n" + "="*60)
        
        choice = input("\n    Select option (1-8): ").strip()
        
        if choice == "1":
            target = input("    Enter target domain or IP: ").strip()
            port_scanner(target)
            
        elif choice == "2":
            target = input("    Enter target domain or IP: ").strip()
            port = input("    Enter port: ").strip()
            banner_grabber(target, port)
            
        elif choice == "3":
            target = input("    Enter target domain or IP: ").strip()
            whois_lookup(target)
            
        elif choice == "4":
            target = input("    Enter target domain or IP: ").strip()
            http_headers(target)
            
        elif choice == "5":
            target = input("    Enter target domain or IP: ").strip()
            ssl_checker(target)
            
        elif choice == "6":
            target = input("    Enter target domain or IP: ").strip()
            subdomain_enum(target)
            
        elif choice == "7":
            target = input("    Enter target domain or IP: ").strip()
            security_headers_scanner(target)
            
        elif choice == "8":
            print("\n    [+] Exiting Toolkit... Goodbye! 🔐\n")
            break
            
        else:
            print("\n    [-] Invalid option. Please choose 1-8")
        
        input("\n    Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n    [+] Interrupted by user. Exiting...\n")
    except Exception as e:
        print(f"\n    [-] Unexpected error: {e}\n")
