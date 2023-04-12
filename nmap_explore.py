"""nmap explore"""

#libs
import nmap

# CONSTANT(s)
NETWORK_RANGE_TARGET = '192.168.1.0/24' #modify the range to scan here
#modify the range you want to scan above.

#function that takes the network range as an input
def scan_network(network_range):
    nm = nmap.PortScanner() #activate nmap PortScanner
    # Nmap performs a ping scan (-sn) on the specified network range
    nm.scan(hosts=network_range, arguments='-sn')

    #iterates through the hosts and checks if there's a hostname
    for host in nm.all_hosts():
        if 'hostnames' in nm[host] and nm[host]['hostnames']: # IF there is a hostname associate with an IP address
            hostname = nm[host]['hostnames'][0]['name']
            if hostname:
                print(f"Host is up: {hostname} ({host})") # print the hostname and IP address

if __name__ == "__main__":
    network_range = NETWORK_RANGE_TARGET
    scan_network(network_range)
