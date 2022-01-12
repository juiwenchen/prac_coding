def factorial(n):
    # n! = n * (n-1) * (n-2)....1
    # n! = n * (n-1)!
    # 0! = 1
    if n == 0:
        return 1

    print(f"{n}")

    return n * factorial(n-1)

def main():
    result = factorial(0)
    print(result)

if __name__ == "__main__":
    main()