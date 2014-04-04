#!/usr/bin/python

import os
import sys
import time
import os.path
import subprocess

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

# This is necessary to get unbuffered output. We want unbuffered output so each line we print gets a
# timestamp from Heroku at the correct time.
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


def execute(command):
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

while True:
    execute(os.path.join(WORKING_DIR, "stockreport.py"))
    time.sleep(60)

