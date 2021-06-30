
num_1 = int(input("Enter first number: "))
num_2 = int(input("enter second number: "))


def gcd(num1, num2):
    while num2 != 0:
        best = num1 % num2
        num1 = num2
        num2 = best
    if num2 == 0:
        return num1
    # return best


print(gcd(num_1, num_2))

