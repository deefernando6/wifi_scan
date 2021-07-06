import scapy.all as scapy
import re

ip_add_range_pattern = re.compile("^:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")