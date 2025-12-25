def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is:", factorial(num))

base = int(input("\nEnter base: "))
exp = int(input("Enter exponent: "))
print("Power result:", power(base, exp))