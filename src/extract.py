#!/bin/python

import csv
import sys

# Put in the path to the file you want in the arguments
filepath = sys.argv[1]

with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)   #This line prints the header row

    # The user is prompted to select the columsn he wants to extract
    selected_columns = []
    selection = input("Enter the index of a column you wish to extract, enter anything that is not a number when done: ")
    
    # We keep asking as long as the input is valid
    while selection.isdigit():
        selected_columns.append(int(selection))
        selection = input("Enter the index of a column you wish to extract, enter anything that is not a number when done: ")

    # We print all the selected headers
    for i in selected_columns:
        print(header_row[i], end=' ')
    print('')

    # And all the data associated with these rows
    for row in reader:
        for i in selected_columns:
            print(row[i], end=' ')
        print('')

