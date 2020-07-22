"""
LOWERCASE AND UPPERCASE MAP

Write a function that creates a dictionary with each (key, value) pair being the
(lower-case, upper-case) versions of a letter, respectively.

- Examples:
    - mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
    - mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
    - mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
    
- Notes:
    - All of the letters in the input list will always be lower-case. 
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in a single input list (of lower-case
      letters) and returns a dictionary of lower-case and upper-case letters
      where the lower-case letters are the "keys" and upper-case letters are the
     "values" within each key/value pair.
     
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "letters"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): dictionary
    - Var Name(s): "letters_dict"
    
- Edge Cases & Constraints:
    - Can the letters in the given input list be upper-case and lower-case?
        - No. All of the letters in the given input list will be lower-case.
    - Can there be duplicate letters in the given input list?
        - Yes. However, there will only be one entry per letter in the output
          dictionary.

****** PLAN ******

****** EXECUTE ****** (Please see below)

"""

def mapping(letters):
    pass

print(mapping(["p", "s"]))  # { "p": "P", "s": "S" }

"""
****** REFLECT/REFACTOR ******

"""