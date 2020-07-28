

def makeArrayConsecutive2(statues):
    print(f"\nstatues = {statues}")
    
    # (1) declare a var, "sizes_dict", and initialize it with an empty
    # dictionary.
    sizes_dict = {}
    print(f"sizes_dict = {sizes_dict}")
    
    # (2) sort the list.
    sorted_statues = sorted(statues)
    print(f"sorted_statues = {sorted_statues}")
    
    # (3) iterate through the "sorted_statues" list and add each element to the
    # "sizes_dict" if it doesn't already exist as a key.
    for k in sorted_statues:
        if k not in sizes_dict:
            sizes_dict[k] = True  
    print(f"***sizes_dict = {sizes_dict}")
    
    # declare a "min_statue_size_size" var and initialize it with the 
    # smallest statue size.
    min_statue_size = sorted_statues[0]
    print(f"min_statue_size = {min_statue_size}")
    
    # declare a "max_statue_size" var and initialize it with the 
    # largest statue size.
    max_statue_size = sorted_statues[-1]
    print(f"max_statue_size = {max_statue_size}")
    
    # declare a "num_of_missing" var and initialize it with a value of 0.
    num_of_missing = 0
    print(f"num_of_missing = {num_of_missing}")
    
    # use a 'for' loop to iterate through the range of numbers between the
    # "min_statue_size" (inclusive) and the "max_statue_size" (exclusive).
    for i in range(min_statue_size, max_statue_size+1, 1):
        # if "i" does NOT exist in the "sizes_dict" as a key, increase the
        # "num_of_missing" by 1.
        if i not in sizes_dict:
            num_of_missing += 1
            print(f"***UPDATED*** num_of_missing = {num_of_missing}")
            
    # return the value of "num_of_missing".
    return num_of_missing
        

print(makeArrayConsecutive2([6, 2, 3, 8]))  # 3