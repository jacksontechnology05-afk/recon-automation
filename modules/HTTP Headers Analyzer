import requests

url = input("Enter target URL (https://example.com): ")

try:

    response = requests.get(url, timeout=5)

    print("\n===================================================")
    print("              HTTP HEADERS ANALYZER")
    print("===================================================\n")

    for header, value in response.headers.items():

        print(f"{header}: {value}")

except Exception as e:

    print(f"\n[-] Error: {e}")
