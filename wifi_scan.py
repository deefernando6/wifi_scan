import scapy.all as scapy
import re

ip_add_range_pattern = re.compile("^:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_address_range_entered = input("\n Please enter the range of the ip addresses which you wanyt to scan (ex: 192.168.1.0/24)")
    if ip_add_range_pattern.search(ip_address_range_entered):
        print(f"{ip_address_range_entered} is valid")
        break