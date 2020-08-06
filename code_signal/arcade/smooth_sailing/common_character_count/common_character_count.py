"""
****** UNDERSTAND Phase ******

Given two strings, find the number of common characters between them.

- Example:
    - Inputs: "aabcc", "adcaa" (2; string data type; "s1" & "s2")
    - Outputs: 3 (1; integer data type; "num_common_chars")
"""
def commonCharacterCount(s1, s2):
    s1_dict = {}
    s1_list = [x for x in s1]
    for i in s1_list:
        if i not in s1_dict:
            s1_dict[i] = 1
        else:
            s1_dict[i] += 1
    s2_dict = {}
    s2_list = [y for y in s2]
    for j in s2_list:
        if j not in s2_dict:
            s2_dict[j] = 1
        else:
            s2_dict[j] += 1
    count = 0
    diff = 0
    for k in s1_dict:
        if k in s2_dict:
            if s1_dict[k] <= s2_dict[k]:
                count += s1_dict[k]
            else:
                count += s2_dict[k]
        
    return count

print(commonCharacterCount("aabcc", "adcaa"))  # 3
print(commonCharacterCount("zzzz", "zzzzzzz"))  # 4