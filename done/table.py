n=int(input("Enter the number to print the table: "))
print("--------------")
for x in range(1,11):
    table=n*x
    #print(table)
    print("|",n,"x",x,"=",table,"|")
    print("--------------")
