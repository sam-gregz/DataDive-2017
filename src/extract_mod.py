#!/bin/python

import csv

def extract(input_file, output_file=""):
    with open(input_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
        # We print the header row with the associated indices
        for i in range(0,len(header_row)):
            print(str(i) + ": " + header_row[i])

        # The user is prompted to select the columsn he wants to extract
        selected_columns = []
        selection = input("Enter the index of a column you wish to extract, enter anything that is not a number when done: ")
    
        # We keep asking as long as the input is valid
        while selection.isdigit():
            if int(selection) >= len(header_row):
                print("This index is out of bounds, make a valid selection")

            else:
                selected_columns.append(int(selection))
                selection = input("Enter the index of a column you wish to extract, enter anything that is not a number when done: ")

        # If an output file is provided, we write the selected columns to it (only supports csv)
        if output_file != "":
            with open(output_file, 'w') as outfile:
                writer = csv.writer(outfile)
            
                new_row = []
                for i in selected_columns:
                    new_row.append(header_row[i])
                writer.writerow(new_row)

                for row in reader:
                    new_row.clear()
                    for i in selected_columns:
                        new_row.append(row[i])
                    writer.writerow(new_row)

        # If no file is specified, we return the output in a dictionary
        else:
            result = []
            
            # We build a dictionary for each row that we put into a list
            row_dict = {}
            for row in reader:
                for i in selected_columns:
                    row_dict[header_row[i]] = row[i]
                result.append(row_dict.copy())
                row_dict.clear()

            return result

