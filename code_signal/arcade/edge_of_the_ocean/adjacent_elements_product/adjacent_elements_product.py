num_arr = [3, 6, -2, -5, 7, 3]


def adjacentElementsProduct(inputArray):
    arr_length = len(inputArray)
    largest_product = []
    if (arr_length >= 2) and (arr_length <= 10):
        i = 0
        j = 1
        while (i < arr_length) and (j < arr_length):
            product = inputArray[i] * inputArray[j]
            # print(product)
            if len(largest_product) > 0:
                if product > largest_product[0]:
                    largest_product.pop(0)
            largest_product.append(product)
            i += 1
            j += 1
    return largest_product[0]
          
print(adjacentElementsProduct(num_arr))