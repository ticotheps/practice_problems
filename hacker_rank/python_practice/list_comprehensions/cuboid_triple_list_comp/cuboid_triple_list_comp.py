# Brute Force Solution
# def print_coordinates(x, y, z, n):
#     possible_coordinates_lst = []
    
#     for i in range(0, x+1):
#         for j in range(0, y+1):
#             for k in range(0, z+1):
#                 if i + j + k != n:
#                     coordinates = [i, j, k]
#                     possible_coordinates_lst.append(coordinates)
                
#     return possible_coordinates_lst

# Alternate Solution with List Comprehensions
def print_coordinates(x, y, z, n):
    return [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n]

print(print_coordinates(1, 1, 2, 3))  # [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]


