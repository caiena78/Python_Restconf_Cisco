import requests
import json
from pprint import pprint
import os


# set up connection parameters in a dictionary
router = {"ip": os.getenv('switch_ip'), "port": "443", "user": os.getenv('switch_user'), "password": os.getenv('switch_pwd')}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

#[area-id=1]
#one vlan by id
#url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-vlan-oper:vlans/vlan=1164"

# list all vlan's
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1%2F0%2F1/"
# print(url)

response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)


api_data = response.json()
print("/" * 50)
print(api_data)