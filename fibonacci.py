def fibonacci_recursion(num_th):
    # [0,1,1,2,3,5,8] is Fibonacci Sequence.
    # F(N) = F(N-1) + F(N-2)
    # time complexity O(2^n)
    # space complexity O(n), the depth of the call stack is N
    if num_th == 0:
        return 0

    if num_th == 1 or num_th == 2:
        return 1
    
    return fibonacci_recursion(num_th - 1) + fibonacci_recursion(num_th - 2)


def fibonacci_dynamic(num_th):
    # time complexity O(n)
    # space complexity O(1), as only three variables are used and the number of that will not changed by the given N
    if num_th == 0:
        return 0

    if num_th <= 2:
        return 1
    
    var_1 = 1 # n -1
    var_2 = 1 # n -2
    var_3 = 0 # n
    for _num in range(1, num_th + 1):
        if _num >= 3:
            var_3 = var_1 + var_2
            var_2 = var_1
            var_1 = var_3
            

    return var_3 
            

def main():
    result = fibonacci_recursion(5)
    print(result)
    result = fibonacci_dynamic(5)
    print(result)

if __name__ == "__main__":
    main()