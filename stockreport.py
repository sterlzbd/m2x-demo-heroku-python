#!/usr/bin/env python

import datetime

import ystockquote
from m2x.client import M2XClient

print("Starting stockreport.py run")

BLUEPRINT_NAME = "stockreport-heroku"

# Load config
APIKEY = open('/app/m2x_api_key.txt').read().strip()
now = datetime.datetime.now()
ATT_Stock_Price = ystockquote.get_price('T')

# Now let's create a blueprint:
client = M2XClient(key=APIKEY)
stockreport_blueprint_exists = False
for blueprint in client.blueprints:
    if blueprint.name == BLUEPRINT_NAME:
        stockreport_blueprint_exists = True
        break

if not stockreport_blueprint_exists:
    blueprint = client.blueprints.create(
        name=BLUEPRINT_NAME,
        description="Stockreport Example Blueprint",
        visibility="private")

# We get the feed that was automatically created when we created the blueprint
feed = blueprint.feed

# Now we need to get the stream for AT&T's stock ticker symbol ("T")
ATT_Stream_Exists = False
for stream in feed.streams:
    if stream.name.upper() == "T":
        ATT_Stream_Exists = True
        break

if not ATT_Stream_Exists:
    stream = feed.streams.create('T')

stream.update(unit={'label': 'Dollars', 'symbol': '$'})

stream.values.add_value(ATT_Stock_Price, now)

print("Ending stockreport.py run")
