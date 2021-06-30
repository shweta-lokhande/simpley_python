fib = [0, 1]


def fibonacci(n):
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]


result =fibonacci(int(input("Enter the number: ")))
print(result)
