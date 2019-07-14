import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Create a dictionary called 'socks_dict' to store unique colors of socks as the
    #     "key" and the tallied count of socks with that color as the "value".
    socks_dict = {}
    # Create an 'entries_count' variable to store the number of entries in the dictionary
    #     and set the value to 0.
    entries_count = 0
    # Create a 'pairs_count' variable to store the number of pairs of socks that can be      #     sold and set the value to 0.    
    pairs_count = 0

    # Loop through the array of sock colors...
    for s in ar:
        # ...Loop through each key in the dictionary...
        for key in socks_dict:
            # ...if the sock color integer ALREADY exists in the dictionary...
            if ar[s] == key:
                # ...increment the existing key's value by 1.
                socks_dict[key] += 1
            # If the sock color integer DOES NOT already exist in the dictionary...
            else:
                # ...add the sock color integer as a NEW entry to the dictionary
                #     and set the value of the new sock to 1.
                socks_dict[ar[s]] = 1
                  
    # Loop through the dictionary...
    for key in socks_dict:
        # If the value of a key is an EVEN integer...
        if socks_dict[key] % 2 == 0:
            # ...increment 'pairs_count' by 1.
            pairs_count += 1
        # If the value of a key is an ODD integer...
        else:
            # ...do nothing.
            pass
    
    # Return 'pairs_count'.
    return pairs_count
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
