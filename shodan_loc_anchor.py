"""shodan with a location anchor"""

#libs
import shodan

#keys
from config import SHODAN_API_KEY

#setup
api_key = SHODAN_API_KEY

shodan_api = shodan.Shodan(api_key)

anchor_ip = '76.176.200.200'  # Mt.Soledad, San Diego, CA
search_radius = 50  # kilometers 


def get_coordinates_from_ip(ip_address):
    try:
        host_info = shodan_api.host(ip_address)
        return host_info.get('latitude'), host_info.get('longitude')
    except shodan.APIError as e:
        print(f"Error: {e}")
        return None, None

latitude, longitude = get_coordinates_from_ip(anchor_ip)
print(f"Anchor IP coordinates: {latitude}, {longitude}")

if latitude and longitude:
    search_query = f"geo:{latitude},{longitude},{search_radius}km"
    print(f"Searching within {search_radius} km of coordinates {latitude}, {longitude}")

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