def con(n):
    inch=2.57
    if(n==0):
        return 0
    else:
        return inch*n
n=float(input("Enter the number: "))
print("total cm is: ",round(con(n),2))