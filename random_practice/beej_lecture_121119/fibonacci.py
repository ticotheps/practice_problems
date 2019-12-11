# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 11):
#     print(n, ':', fibonacci(n))
    
# for n in range(1, 101):
#     print(n, ':', fibonacci(n))
    
# memoization -> store calculated values in a dictionary for later use to make
# future calculations faster.

fib_cache = {}

def fibonacci(n):
    # If we have cached the value already, then return it
    if n in fib_cache:
        return fib_cache[n]
    
    # If a cached value for 'n' does not exist, compute it
    if n == 0 or n == 1:
        fib_num = n
    elif n == 2:
        fib_num = 1
    elif n > 2:
        fib_num = fibonacci(n-1) + fibonacci(n-2)
    
    # Cache the value and return it
    fib_cache[n] = fib_num
    return fib_num   
 
for n in range(1, 101):
    print(n, ':', fibonacci(n))