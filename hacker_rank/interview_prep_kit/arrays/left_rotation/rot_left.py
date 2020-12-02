#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    input_list_dict = {}
    
    # create entries for dict where keys = 'values of given input list' and
    # values = 'indices of corresponding values from the given input list'.
    for i in range(0, len(a)):
        input_list_dict[a[i]] = i
    
    # print("input_list_dict = ", input_list_dict)
        
    # implement rotations for each 'key' in the dict (which actually represents
    # a value from the original given input list).
    for key in input_list_dict:
        input_list_dict[key] -= d

    # print("input_list_dict = ", input_list_dict)
    
    # creating a new variable in which to keep track of the rotated values from
    # the given input list      
    rotated_input_list = [0] * len(a)
    for key in input_list_dict:
        rotated_input_list[input_list_dict[key]] = key

    # print("rotated_input_list = ", rotated_input_list)    
    
    rotated_input_list_str = ""
    
    for elem in rotated_input_list:
        new_addition = f"{elem} "
        rotated_input_list_str += new_addition    
    
    return(rotated_input_list)
    
# rotLeft([7, 4, 9, 8, 1], 2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()