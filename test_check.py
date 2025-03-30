import requests

serial = "92uA689185"  # Change this to any serial number for testing
url = f"http://127.0.0.1:5000/check_serial/{serial}"

response = requests.get(url)
print(response.json())
