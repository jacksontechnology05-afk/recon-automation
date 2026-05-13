import requests

subdomains = ["www", "mail", "ftp", "test"]

domain = input("Enter domain: ")

for sub in subdomains:
    url = f"http://{sub}.{domain}"

    try:
        requests.get(url)
        print(f"[+] Found: {url}")
    except requests.ConnectionError:
        pass
