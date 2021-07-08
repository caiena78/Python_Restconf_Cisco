import requests
#from pprint import pprint
import os
import json
import os
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# set up connection parameters in a dictionary
router = {"ip": os.getenv('switch_ip'), "port": "443", "user": os.getenv('switch_user'), "password": os.getenv('switch_pwd')}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

#[area-id=1]


# list all vlan's
#url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data/common-oper-data=00:0e:8e:84:d3:9f"
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data"
# print(url)

response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)


api_data = response.json()
#print("/" * 50)
print(json.dumps(api_data,sort_keys=True, indent=4))
