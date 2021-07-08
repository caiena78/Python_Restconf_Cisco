import requests
import json
from pprint import pprint
import os
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# set up connection parameters in a dictionary
router = {"ip": os.getenv('switch_ip'), "port": "443", "user": os.getenv('switch_user'), "password": os.getenv('switch_pwd')}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}


id="1%2F0%2F20" #1/0/20 %2f=/
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={id}/shutdown"    
print(url)


#you will get a 204 if it enabled the interface you get a 404 if its alread enabled
response = requests.delete(url,headers=headers,auth=(router['user'], router['password']),verify=False)
print(response)
if response.status_code==204:
    print("Interface was enabled")
if response.status_code==404:
    print("Interface was already enable")
