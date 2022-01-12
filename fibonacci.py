"""Fibonacci Sequece

The sequece is like the following:
0,1,1,2,3,5,8,13,21 ...

Consider the first element is index 0

when index is greater than 1, the index N is (N-1) + (N-2)

Two ways to solve it:
    1. recursion 
    2. dynamic programming
"""
def fibonacci_recursion(index: int)-> int:
    # time complexity O(2^n)
    # space complexity O(n), the depth of the call stack is N
    if index == 0:
        return 0
    elif index == 1:
        return 1
    
    return fibonacci_recursion(index - 1) + fibonacci_recursion(index - 2)

def fibonacci_dynamic(index: int)-> int:
    # time complexity O(n)
    # space complexity O(1), as only three variables are used and the number of that will not changed by the given N
    if index == 0:
        return 0
    elif index == 1:
        return 1

    n_1 = 1 # n-1
    n_2 = 0 # n-2
    sum = 0 # n
    for number in range(0, index + 1, 1):
        if number > 1:
            sum = n_1 + n_2
        # update n_1 and n_2 for the next loop
            n_2 = n_1
            n_1 = sum
    
    return sum

def main():
    result = fibonacci_recursion(10)
    print(result)
    result = fibonacci_dynamic(10)
    print(result)


if __name__ == "__main__":
    main()