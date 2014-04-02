#!/usr/bin/python

import os
import sys
import time
import os.path
import subprocess


WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

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
    # execute(loadreport.rb)
    time.sleep(60)

