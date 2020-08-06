"""
****** UNDERSTAND Phase ******

Given two strings, find the number of common characters between them.

- Example:
    - Inputs: "aabcc", "adcaa" (2; string data type; "s1" & "s2")
    - Outputs: 3 (1; integer data type; "num_common_chars")
"""
def commonCharacterCount(s1, s2):
    s1_dict = {}
    print(f"\ns1_dict = {s1_dict}")
    
    s1_list = [x for x in s1]
    print(f"s1_list = {s1_list}")
    
    for i in s1_list:
        if i not in s1_dict:
            s1_dict[i] = 1
        else:
            s1_dict[i] += 1
    print(f"*s1_dict = {s1_dict}")
    
    s2_dict = {}
    print(f"s2_dict = {s2_dict}")
    
    s2_list = [y for y in s2]
    print(f"\ns2_list = {s2_list}")
    
    for j in s2_list:
        if j not in s2_dict:
            s2_dict[j] = 1
        else:
            s2_dict[j] += 1
    print(f"*s2_dict = {s2_dict}")
    
    # declare a "count" var to keep track of the number of common characters
    count = 0
    print(f"count = {count}")
    
    diff = 0
    print(f"diff = {diff}")
    
    for k in s1_dict:
        if k in s2_dict:
            if s1_dict[k] <= s2_dict[k]:
                count += s1_dict[k]
            else:
                count += s2_dict[k]
        
    return count

print(commonCharacterCount("aabcc", "adcaa"))  # 3
print(commonCharacterCount("zzzz", "zzzzzzz"))  # 4