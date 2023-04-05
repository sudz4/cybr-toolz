import ipaddress
import requests

def is_vpn_used():
    # Get the IP address being used by the device
    ip_address = requests.get('https://api.ipify.org').text
    
    # Check if the IP address belongs to a known VPN provider
    vpn_ips = [
        ipaddress.IPv4Network('103.192.152.0/22'),  # ExpressVPN
        ipaddress.IPv4Network('45.65.0.0/20'),     # NordVPN
        ipaddress.IPv4Network('198.18.0.0/15'),    # Private Internet Access
        ipaddress.IPv4Network('185.159.131.0/24'), # Proton VPN
        ipaddress.IPv4Network('185.159.132.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.136.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.140.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.144.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.148.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.152.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.156.0/22'), # Sweden (SE) - Proton VPN
        ipaddress.IPv4Network('185.159.160.0/22'), # Proton VPN
        ipaddress.IPv4Network('185.159.164.0/22'), # Proton VPN
        ipaddress.IPv4Network('45.134.140.0/22'), # I addded this (matt 4/4/23)

# 185.159.168.0/22
# 185.159.172.0/22
# 185.159.176.0/22
# 185.159.180.0/22
# 185.159.184.0/22
# 185.159.188.0/22

        # Add more VPN IP address ranges as needed
    ]
    
    for vpn_ip in vpn_ips:
        if ipaddress.IPv4Address(ip_address) in vpn_ip:
            return True
    
    return False

if is_vpn_used():
    print("A VPN is being used")
else:
    print("No VPN detected")

