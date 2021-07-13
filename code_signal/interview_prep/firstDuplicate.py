def firstDuplicate(a):
    num_of_duplicates = 0
    duplicate_value = -1
    duplicates_dict = {}
    lowest_second_index = -1
    
# Figure out how many duplicate values exist in the given array.
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if i < j and a[i] == a[j]:
                print(f"a[{i}] = ", a[i])
                print(f"a[{j}] = ", a[j])
                print("We have a match!\n")
                # Increase the running count of duplicates.
                num_of_duplicates += 1
                # Store the duplicate value.
                duplicate_value = a[i]
                # Create a new entry in the 'duplicates_dict' dictionary if it doesn't already exist.
                if a[i] in duplicates_dict:
                    if j < duplicates_dict[a[i]]:
                        duplicates_dict[a[i]] = j
                else:
                    duplicates_dict[a[i]] = j
    # if 0 duplicates exist, return -1.
    # if 1 duplicate exists, return the value of that item.
    if num_of_duplicates <= 1:
        return duplicate_value
    # if 2 or more duplicates exist, return the value of the item which 
    # has the LOWEST index for its second occurrence.
    for key in duplicates_dict:
        print("key = ", key,)
        print(f"duplicates_dict[{key}] = ", duplicates_dict[key])
        if lowest_second_index == -1 or duplicates_dict[key] < lowest_second_index:
            lowest_second_index = duplicates_dict[key]
            print("lowest_second_index = ", lowest_second_index)
            duplicate_value = key
            print("duplicate_value = ", duplicate_value, "\n")
            print("duplicates_dict = ", duplicates_dict)
    print("output value: ", duplicate_value)
    return duplicate_value

firstDuplicate([2, 1, 3, 5, 3, 2])