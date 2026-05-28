def sum(n):
    if(n==1):
        return 1
    else:
        temp= (n*(n+1))/2
        return temp
n=int(input("ENter the number: "))
print("Sum of n natural number are",sum(n))