def firstDuplicate(a):
    num_of_duplicates = 0
    duplicate_value = -1
    occurrences_dict = {}
    lowest_second_index = -1
    
    # Figure out how many duplicate values exist in the given array.
    for i in range(0, len(a)):
        # If an iterated-on item does not exist in the dictionary, create a new entry for it.
        if a[i] not in occurrences_dict:
            occurrences_dict[a[i]] = False
        # If an iterated-on item already exists in the dictionary, change the value from True to the index of the second occurrence
        # of that item.
        else:
            if occurrences_dict[a[i]] == False:
                occurrences_dict[a[i]] = i
                num_of_duplicates += 1
                duplicate_value = a[i]
        
    # if 0 duplicates exist, return -1.
    # if 1 duplicate exists, return the value of that item.
    if num_of_duplicates <= 1:
        return duplicate_value

    # if 2 or more duplicates exist, return the value of the item which 
    # has the LOWEST index for its second occurrence.
    
    for key in occurrences_dict:
        if type(occurrences_dict[key]) is int:
            if lowest_second_index == -1 or occurrences_dict[key] < lowest_second_index:
                lowest_second_index = occurrences_dict[key]
                duplicate_value = key
    
    print("output value: ", duplicate_value)
    return duplicate_value

arr = [1, 1, 2, 2, 1]
firstDuplicate(arr)