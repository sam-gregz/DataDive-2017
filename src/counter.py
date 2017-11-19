#!/bin/python
from extract_mod import extract

path = "/home/sam/Documents/DataDive/Transportation/NYC General Transport/NYC-vehicle-collisions.csv"
rows = extract(path, selected_columns=[3])

counter = {}

for row in rows:
    if row["BOROUGH"] in counter:
        counter[row["BOROUGH"]] = counter[row["BOROUGH"]] + 1
    else:
        counter[row["BOROUGH"]] = 0

for borough in counter:
    print(borough + ": " + str(counter[borough]))
