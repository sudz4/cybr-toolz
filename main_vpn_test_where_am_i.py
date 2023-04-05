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

# error handling
"""
Merge (default): This option creates a merge commit when pulling changes from the remote repository. 

To set the default preference for all repositories, you can replace git config with git config --global. 
Once you have configured the desired merge strategy, you can perform a git pull to update your local branch 
with the changes from the remote repository.

git config pull.rebase false
git pull
"""
