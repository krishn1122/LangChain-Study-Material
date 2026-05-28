n=int(input("Enter the lenth of nth series: "))
def fibonacci(n):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum(n):
    add=(n*(n+1))/2
    return add

print(f"fibonacci series is:{fibonacci(9)}")
print(f"sum of n natural number is:{sum(n)}")

