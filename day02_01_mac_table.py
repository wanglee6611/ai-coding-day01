import re

mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

pattern = r"(\d+)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+([A-Z]+)\s+(\S+)"
match = re.match(pattern, mac_table)

if match:
    print("{:<6}: {}".format("VLAN", match.group(1)))
    print("{:<6}: {}".format("MAC", match.group(2)))
    print("{:<6}: {}".format("Type", match.group(3)))
    print("{:<6}: {}".format("Intf", match.group(4)))