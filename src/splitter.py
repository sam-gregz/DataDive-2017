#!/bin/python

import random

# Splits a list of data into two lists in a ratio of (fraction):(1-fraction) randomly
def data_split(data, fraction):
    # Since shuffle affects the list and we want to keep the original list intact, we copy the list
    shf_data = data.copy()
    shuffle(shf_data)
    
    # We will return a list containing 2 lists
    result = []

    # This is the first list of the result, containing the training data
    train_data = []
    train_size = fraction * len(shf_data)
    for row in shf_data[:train_size]:
        train_data.append(row.copy())
    result.append(train_data.copy())

    # This is the second list of the result, containing the testing data
    test_data = []
    for row in shf_data[train_size:]:
        test_data.append(row.copy())
    result.append(test_data.copy())

    return result
