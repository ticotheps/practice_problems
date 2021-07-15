def firstNotRepeatingCharacter(s):
    
    # Create a var that stores the to-be-returned-character, which will have a
    # default value of '_'.
    non_repeat_char = '_'

    # Create a var to store occurrences of specific values inside of a dict.
    repeating_chars_dict = {}

    # Iterate through given input list and document each occurrence in dict.
    for i in range(0, len(s)):
        item = s[i]
        # print(f"item = {item}")
        
        if item not in repeating_chars_dict:
            # print(f"'{item}' was just added as a new key to the dict.")
            repeating_chars_dict[s[i]] = False
            # print(f"repeating_chars_dict = {repeating_chars_dict}\n")
        else:
            # print(f"The value for the '{item}' key was just changed to 'True'.")
            repeating_chars_dict[s[i]] = True
            # print(f"repeating_chars_dict = {repeating_chars_dict}\n")

    # Iterate through given input list and cross-reference with dict to find 
    # first NON-REPEATING character.
    for j in range(0, len(s)):
        item = s[j]
        
        if repeating_chars_dict[item] == False:
            non_repeat_char = item
            break

    # Return NON-REPEATING character.
    print(non_repeat_char)
    return non_repeat_char


s = "abacabad"
firstNotRepeatingCharacter(s)