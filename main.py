#! /usr/bin/env python
import netifaces
from datetime import datetime

import requests


# List the interfaces which connect to the internet.
interfaces = ["wlan0", "eth0"]

# Api keys for freedns (http://freedns.afraid.org/dynamic/update.php?API_KEY)
api_keys = ["API_KEY_1",
            "API_KEY_2"]
update_url = "http://freedns.afraid.org/dynamic/update.php?"

logfile = "/var/log/freedns.log"
handle = open(logfile, mode='a')
connected = False

for interface in interfaces:
    if netifaces.ifaddresses(interface).get(netifaces.AF_INET):
        connected = True
        break
if connected:
    try:
        for api_key in api_keys:
            response = requests.get(update_url + api_key)
            handle.write(str(datetime.now()) + " " + api_key + " " + response.text.strip() + "\n")
    except Exception, e:
        handle.write(e.message.strip() + "\n")

else:
    handle.write(str(datetime.now()) + " Network disconnected\n")

handle.close()