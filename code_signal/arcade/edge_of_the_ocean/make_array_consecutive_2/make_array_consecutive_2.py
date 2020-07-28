

def makeArrayConsecutive2(statues):
    sizes_dict = {}
    sorted_statues = sorted(statues)

    for k in sorted_statues:
        if k not in sizes_dict:
            sizes_dict[k] = True  

    min_statue_size = sorted_statues[0]

    max_statue_size = sorted_statues[-1]

    num_of_missing = 0

    for i in range(min_statue_size, max_statue_size+1, 1):
        if i not in sizes_dict:
            num_of_missing += 1
    return num_of_missing
