#!/usr/bin/env python

from requests.exceptions import HTTPError
from datetime import datetime

import ystockquote
from m2x.client import M2XClient


def post_stock_price(symbol, apikey, devicename):
    '''
    Retrieve the stock price for the given ticker symbol ("T" for AT&T) and
    post it in the correct M2X data stream.
    '''
    client = M2XClient(key=apikey)

    # Find the correct device if it exists, if not create it.
    try:
        device = [d for d in client.devices(q=devicename) if d.name == devicename][0]
    except IndexError:
        device = client.create_device(name=devicename,
                                      description="Stockreport Example Device",
                                      visibility="private")

    # Get the stream if it exists, if not create the stream.
    try:
        stream = device.stream(symbol)
    except HTTPError:
        stream = device.create_stream(symbol)
        device.update_stream(symbol, unit={'label': 'Dollars', 'symbol': '$'})

    postime = datetime.now()
    stock_price = ystockquote.get_price(symbol).encode('utf-8')
    stream.add_value(stock_price, postime)
