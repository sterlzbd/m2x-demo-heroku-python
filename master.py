#!/usr/bin/env python

import os
import sys
import time
from stockreport import post_stock_price


DEVICE_NAME = os.environ.get('DEVICE_NAME', 'stockreport-heroku')

APIKEY = os.environ['MASTER_API_KEY']

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)


while True:
    print "Posting stock prices."
    # Post stock price of AT&T
    post_stock_price("T", APIKEY, DEVICE_NAME)
    print "Stock prices posted."
    time.sleep(60)

