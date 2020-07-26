num_arr = [3, 6, -2, -5, 7, 3]

def adjacentElementsProduct(inputArray):
    largest_product = None
    print(f"largest_product = {largest_product}")
    
    for i in range(0, len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        print(f"product = {product}")
        
        if largest_product == None or product > largest_product:
            largest_product = product
            
    return largest_product
          
print(adjacentElementsProduct(num_arr))  # 21