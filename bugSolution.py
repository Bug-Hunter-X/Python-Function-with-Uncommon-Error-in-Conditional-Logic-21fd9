def function_with_uncommon_error_solution(x, y):
    if x == 0 and y == 0:
        return 0 # Handle the case where both x and y are zero
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x / y

result = function_with_uncommon_error_solution(0, 0)
print(result) # Output: 0

result = function_with_uncommon_error_solution(5, 0)
print(result) # Output: 5

result = function_with_uncommon_error_solution(0, 5)
print(result) # Output: 5

result = function_with_uncommon_error_solution(10, 2)
print(result) # Output: 5.0