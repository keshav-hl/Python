#Recursion in python/
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
n = int(input("Enter the factorial number: "))
print(factorial(n))

#Example-2 for recursion/
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter teh fibonacci number: "))
print(fibonacci(n))