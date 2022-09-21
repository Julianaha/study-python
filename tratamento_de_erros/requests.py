import requests

try:
    result = requests.get("https://www.google.com/")
    result.raise_for_status()
    print("Site Google está acessível")
except Exception as error:
    print(f"Site Google está inacessível. Error: {error.__cause__}")
