import requests

# API endpoint URL
url = "https://ipapi.co/json/"

# Make a GET request to the API endpoint
response = requests.get(url)

# Check the response status code
if response.status_code != 200:
    print("Error: Unable to retrieve IP information.")
    exit()

# Parse the JSON response
data = response.json()

# Print the IP ianformation
print()
print("IP address:", data["ip"])
print("Country:", data["country_name"], "(" + data["country_code"] + ")")
print("Region:", data["region"])
print("City:", data["city"])
print("Latitude:", data["latitude"])
print("Longitude:", data["longitude"])
print("Time zone:", data["timezone"])
