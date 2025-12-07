import sys
import requests


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    amount = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

url = "https://api.coincap.io/v2/assets/bitcoin"
API_KEY = "643ee3bc72dd5ae8093553b6757bdbe8423e38032f5cfa22551c86f705d7c63d"


headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    print("API request failed")
    sys.exit(1)

total = price * amount

print(f"${total:,.4f}")
