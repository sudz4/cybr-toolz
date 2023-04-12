"""shodan explore"""

#libs
import shodan

#keys
from config import SHODAN_API_KEY

#setup
api_key = SHODAN_API_KEY
shodan_api = shodan.Shodan(api_key)

#perform a basic shodan scan

search_query = 'product:"Apache httpd"'

try:
    results = shodan_api.search(search_query)

    print(f"Results found: {results['total']}")
    for result in results['matches']:
        print(f"IP: {result['ip_str']}")
        print(f"Port: {result['port']}")
        print(f"Hostnames: {', '.join(result['hostnames'])}")
        print(f"Data: {result['data']}")
        print()

except shodan.APIError as e:
    print(f"Error: {e}")

