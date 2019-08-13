num_arr = [1, 2, 3, 4]

def adjacentElementsProduct(inputArray):
    arr_length = len(inputArray)
    largest_product = 0
    if (arr_length >= 2) and (arr_length <= 10):
        for i in range(arr_length):
            for j in range(i+1, arr_length):
                product = inputArray[i] * inputArray[j]
                # print(product)
                if product > largest_product:
                    largest_product = product
    return largest_product
          
print(adjacentElementsProduct(num_arr))