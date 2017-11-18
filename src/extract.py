#!/bin/python

import csv
import sys

# Put in the path to the file you want in the arguments
filepath = sys.argv[1]

with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)   #This line prints the header row
