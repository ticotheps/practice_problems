import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Create a dictionary called 'socks_dict' to store unique colors of socks as the
    #     "key" and the tallied count of socks with that color as the "value".
    socks_dict = dict()
    # print(f'socks_dict: {socks_dict}')
    # Create a 'pairs_count' variable to store the number of pairs of socks that can be      #     sold and set the value to 0.    
    pairs_count = 0
    # print(f'pairs_count: {pairs_count}')
    # Loop through the array of sock colors...
    for s in range(n):
        # print(f's in ar: {ar[s]}')
        # ...Loop through each key in the dictionary, if the sock color
        #     integer ALREADY exists in the dictionary...
        if ar[s] in socks_dict:
            # print(f's in socks_dict.keys: {ar[s]}')
            # ...increment the existing key's value by 1.
            socks_dict[ar[s]] += 1
            # If the sock color integer DOES NOT already exist in the dictionary...
        else:
            # ...add the sock color integer as a NEW entry to the dictionary
            #     and set the value of the new sock to 1.
            socks_dict[ar[s]] = 1
                  
    # Loop through the dictionary...
    for key in socks_dict:
        # If the value of a key is an EVEN integer...
        if socks_dict[key] % 2 == 0:
            # ...create a variable 'even_pairs' that stores the number of
            #     pairs for that color.
            even_pairs = socks_dict[key] / 2
            # ...if the 'even_pairs' for a color is >= 1...
            if even_pairs >= 1:
                # ...increment 'pairs_count' by the integer of 'even_pairs'.
                pairs_count += int(even_pairs)
            # ...if the 'even_pairs' for a color is < 1...
            else:
                # ...increment 'pairs_count' only by 1.
                pairs_count += 1
        # If the value of a key is an ODD integer...
        if socks_dict[key] % 2 != 0:
            # ...create a variable 'odd_pairs' that stores the number of
            #     pairs for that color...
            # ...and divide 'socks_dict[key]' by 2 and round down, adding
            odd_pairs = math.floor(socks_dict[key] / 2)
            # ...increment 'pairs_count' by the integer of 'odd_pairs'.
            pairs_count += int(odd_pairs)
           
    # Return 'pairs_count'.
    # print(socks_dict)
    return f'pairs_count: {pairs_count}'
        
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
