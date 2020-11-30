# Optimized Solution
# Time Complexity: O(n) | Space Complexity: O(n)
def arrayOfProducts(array):
    resulting_lst = [1] * len(array)
    print("resulting_lst = ", resulting_lst)
    
    left_products_lst = [1] * len(array)
    print("left_products_lst = ", left_products_lst)
    
    right_products_lst = [1] * len(array)
    print("right_products_lst = ", right_products_lst)
    
    left_running_product = 1
    for i in range(0, len(array)):
        left_products_lst[i] = left_running_product
        left_running_product *= array[i]
    
    right_running_product = 1
    for j in range(len(array)-1, -1, -1):
        right_products_lst[j] = right_running_product
        right_running_product *= array[j]
        
    for k in range(0, len(resulting_lst)):
        total_product = left_products_lst[k] * right_products_lst[k]
        resulting_lst[k] = total_product
        
    print("resulting_lst = ", resulting_lst)
    return resulting_lst