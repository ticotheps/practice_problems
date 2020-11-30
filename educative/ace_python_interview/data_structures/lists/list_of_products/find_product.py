"""
LIST OF PRODUCTS OF ALL ELEMENTS

Given a list, modify it so that each index stores the product of all elements in
the list except the element at the index itself.

Input:
    - A list of numbers (could be floating point or integers).
    
Output:
    - A list such that each index has a product of all the numbers in the list
    except the number stored at that index.
    
Sample Input/Output #1:
    - Input arr = [1, 2, 3, 4]
    - Output arr = [24, 12, 8, 6]
    
Sample Input/Output #2:
    - Input arr = [4, 2, 1, 5, 0]
    - Output arr = [0, 0, 0, 0, 40]
"""

"""
U.P.E.R. Problem-Solving Framework

UNDERSTAND Phase:
    - Objective: 
        - Write an algorithm that takes in a single input list (containing integers
        or floating point numbers) and returns a single output list such that each
        index contains the product of all the numbers in the list except the number
        at that index.
        
    - Inputs:
        - Expecting: 1
        - Data Type: list
        - Var Name: "lst"
        
    - Outputs:
        - Expecting: 1
        - Data Type: list
        - Var Name: "lst_of_products"
        
    - Constraints & Edge Cases:
        - Can elements in the given input list be negative numbers?
            - Yes.
        - Can elements in the given input list be floating point numbers?
            - Yes. This is clearly stated in the prompt.
        - Can the given input list be empty?
            - No. Products cannot be calculated without factors.
            
PLAN Phase:
    - Brute Force Solution:
        - Iterate through the given input list twice using nested 'for' loops.
        - The inner 'for' loop will allow us to have access to the other values while
        being able to modify the value at the index of the outer 'for' loop.
        - The modification to this value will include finding the product of all the
        other values at each index. 
        - This will produce sub-par time complexity, but will get the job done until
        it can be optimized later.
"""

# EXECUTE Phase

# Brute Force Solution
def find_product(lst):
    # Declare a new var, 'output_lst', and initialize it with a value of '[]'.
    output_lst = []

    # Iterate through the given input list.
    for i in range(0, len(lst)):
        product_of_other_indices = 1   
        for j in range(0, len(lst)):
            if j != i:
                product_of_other_indices *= lst[j]
        output_lst.append(product_of_other_indices)
    return output_lst        

"""
REFLECT/REFACTOR Phase
    - Asymptotic Analysis:
        - Time Complexity: O(n^2) -> "quadratic time"
        - Space Comlexity: O(n) -> "linear space"
        
    - Can the time or space complexity of this brute force solution be improved upon?
        - Yes. The time complexity could be improved to O(n), linear time.
    
    - If yes, how?
        - Instead of using nested 'for' loops to gain access to a particular index AS WELL AS to the values at all the other indices, we can traverse through the list three times (at O(n) time complexity for each iteration), once going from left to right, another time going from right to left, and one more time through the "resulting_lst" where we will combine the products to the left and right at a given index.
        
        - Create a new "resulting_lst" variable that is set to a new list of equal size as the given input array and is initialized with a value of 1 for each element to start off.
        
        - While iterating through the given input list from left to right, we will keep track of the total product of all elements to the left of that particular index in a variable called "left_running_product".
        
        - While iterating through the given input list from right to left, we will keep track of the total product of all elements to the right of that particular index in a variable called "right_running_product".
        
        - During each of these iterations, we will be multiplying each element in the "resulting_lst" by the corresponding running total value at the given index.
        
        - Lastly, we will iterate through the "resulting_lst" and access the values of both "left_products_lst" and "right_products_lst" at the same time and multiply them together before setting the value of the given index in the "resulting_lst" list to that total product.
"""

# Optimized Solution
# Time Complexity: O(n) | Space Complexity: O(n)
def find_product_optimized(lst):
    resulting_lst = [1] * len(lst)
    print("resulting_lst = ", resulting_lst)
    
    left_products_lst = [1] * len(lst)
    print("left_products_lst = ", left_products_lst)
    
    right_products_lst = [1] * len(lst)
    print("right_products_lst = ", right_products_lst)
    
    left_running_product = 1
    for i in range(0, len(lst)):
        left_products_lst[i] = left_running_product
        left_running_product *= lst[i]
    
    right_running_product = 1
    for j in range(len(lst)-1, -1, -1):
        right_products_lst[j] = right_running_product
        right_running_product *= lst[j]
        
    for k in range(0, len(resulting_lst)):
        total_product = left_products_lst[k] * right_products_lst[k]
        resulting_lst[k] = total_product
        
    print("resulting_lst = ", resulting_lst)
    return resulting_lst
        
        
        