#!/usr/bin/env python

import sys
import time
import os.path
import datetime

import ystockquote
from m2x.client import M2XClient

# This is necessary to get unbuffered output. We want unbuffered output so each line we print gets a
# timestamp from Heroku at the correct time. Otherwise all will have the same timestamp when the program exits.
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)
sys.stderr = Unbuffered(sys.stderr)


print("Starting stockreport.py run")
DEVICE_NAME = "stockreport-heroku"
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

APIKEY = open(os.path.join(WORKING_DIR, 'm2x_api_key.txt')).read().strip()
NOW = datetime.datetime.now()
ATT_STOCK_PRICE = ystockquote.get_price('T')

# Now let's create a device:
client = M2XClient(key=APIKEY)
stockreport_device_exists = False
for device in client.devices:
    if device.name == DEVICE_NAME:
        stockreport_device_exists = True
        break

if not stockreport_device_exists:
    device = client.devices.create(
        name=DEVICE_NAME,
        description="Stockreport Example Device",
        visibility="private")

# Now we need to get the stream for AT&T's stock ticker symbol ("T")
ATT_Stream_Exists = False
for stream in device.streams:
    if stream.name.upper() == "T":
        ATT_Stream_Exists = True
        break

if not ATT_Stream_Exists:
    stream = device.streams.create('T')

stream.update(unit={'label': 'Dollars', 'symbol': '$'})

stream.values.add_value(ATT_STOCK_PRICE, NOW)

print("Ending stockreport.py run")
