""""
WHICH NUMBER IS NOT LIKE THE OTHERS?

Create a function that takes in a list of numbers and returns the unique number
in that list.

NOTES:
    - Test cases will always have exactly one unique number while all others are
    the same.
"""

"""
The U.P.E.R. Problem-Solving Framework

U = UNDERSTAND the problem

- Objective:
    - Write an algorithm, 'find_unique_num()', that takes in a single input 
    list, 'lst', and returns the only unique integer in that list as a single 
    output, 'unique_num'.
      
- Expected Input:
    - Number Of: 1
    - Data Type: list
    - Var Name: 'lst'
    
- Expected Output:
    - Number Of: 1
    - Data Type: integer
    - Var Name: 'unique_num'
    
- Edge Cases & Constraints:
    - Can the elements in the given input list be negative numbers?
        - Yes.
    - Can the elements in the given input list be floating point numbers?
        - Yes.
    - Can the elements in the given input list be empty strings?
        - No. The elements must be positive, whole integers.

P = devise a PLAN (please see below)
E = EXECUTE the plan (please see below)
"""
# Brute Force Solution
def find_unique_num(lst):
	unique_num = None

	for i in range(0, len(lst)):
		for j in range(i+1, len(lst)):
   
			if lst[0] != lst[1] and lst[0] != lst[2]:
				unique_num = lst[0]
				return unique_num

			if lst[i] != lst[j]:
				unique_num = lst[j]
				return unique_num
	return 'There are no unique numbers in the given input list'

print(find_unique_num([3, 3, 3, 7, 3, 3]))           # 7
print(find_unique_num([0, 0, 0.77, 0, 0]))           # 0.77
print(find_unique_num([0, 1, 1, 1, 1, 1, 1, 1]))     # 0
print(find_unique_num([-4, -4, -4, 4]))              # 4
print(find_unique_num([8, 8, 8, 8, 8, 8, 8, 0.5]))   # 0.5
print(find_unique_num([2, 1, 2, 2, 2, 2, 2, 2]))     # 1

"""
R = REFLECT/REFACTOR the plan
- Asymptotic Analysis:
	- Brute Force Solution:
		- Time Complexity: O(n^2) -> 'quadratic time'
		- Space Complexity: O(1) -> 'constant space'
  
- Could the time/space complexity of your Brute Force Solution be improved?
    - Yes.
    
- If so, how?
    - Instead of using nested 'for' loops to compare numbers in the given input
      list to each other, we could use a cache object/dictionary that would
      store key:value pairs that we've already encountered before.
    - Using a cache object/dictionary would improve the time complexity from
      "quadratic" to "linear" because there would only be a single "for" loop
      instead of nested "for" loops.
    - The tradeoff here would be the worsened space complexity. With the
      creation of a cache object/dictionary, this would require more space in
      memory, thereby depending on the number of entries that we added into the
      cache object/dictionary. Therefore, the new space complexity for the
      optimized solution would be "linear" (instead of "constant").
"""

# Optimized Solution
def find_unique_num_optimized(lst):
	unique_num = None

	for i in range(0, len(lst)):
		for j in range(i+1, len(lst)):
   
			if lst[0] != lst[1] and lst[0] != lst[2]:
				unique_num = lst[0]
				return unique_num

			if lst[i] != lst[j]:
				unique_num = lst[j]
				return unique_num
	return 'There are no unique numbers in the given input list'

print(find_unique_num_optimized([3, 3, 3, 7, 3, 3]))           # 7
print(find_unique_num_optimized([0, 0, 0.77, 0, 0]))           # 0.77
print(find_unique_num_optimized([0, 1, 1, 1, 1, 1, 1, 1]))     # 0
print(find_unique_num_optimized([-4, -4, -4, 4]))              # 4
print(find_unique_num_optimized([8, 8, 8, 8, 8, 8, 8, 0.5]))   # 0.5
print(find_unique_num_optimized([2, 1, 2, 2, 2, 2, 2, 2]))     # 1