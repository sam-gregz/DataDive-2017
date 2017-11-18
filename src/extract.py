#!/bin/python

import csv
import sys

filepath = sys.argv[1]
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
