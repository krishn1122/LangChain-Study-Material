n=int(input("Enter the value of n: "))

for i in range (1,n+1):
  print(" "*(n-i),end=' ')
  print("* "*(2*i-i),end=' ')
  print(" ")

for i in range (1,n+2):
  for j in range(1,n+2):
    print("*",end=' ')
  print()

for i in range (n,0,-1):
  print(" "*(n-i),end=' ')
  print("* "*(2*i-i),end=' ')
  print(" ")

for y in range(-n, n + 1):
    for x in range(-n, n + 1):

        # Distance from center
        value = x*x + y*y

        # Print boundary only
        if n*n - n <= value <= n*n + n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(1,n+1):
  for j in range(1,n+2):
    print("*",end=' ')
  print()

for i in range (1,n):
  print(" "*(n-i),end=' ')
  print("+ "*(2*i-i),end=' ')
  print(" ")
for i in range (n,1,-1):
  print(" "*(n-i),end=' ')
  print("+ "*(2*i-i),end=' ')
  print(" ")
for i in range (1,4):
  print(" "*(4-i),end=' ')
  print(" +"*(2*i-i),end=' ')
  print("  ")

print("------------------------")
for i in range (n,0,-1):
  print("*"*(2*i-i),end=' ')
  print(" "*(n-i),end=' ')
  print("")
for i in range (2,n+1):
  print("*"*(2*i-i),end=' ')
  print(" "*(n-i),end=' ')
  print("")

print("------------------------")

for i in range (1,n+1):
  for j in range (1,n+1):
    print("*", end='')
  print()
for i in range (2,n+1):
  print("*"*(2*i-i),end=' ')
  print(" "*(n-i),end=' ')
  print("")

print("------------------------")
# I
for i in range(1,n+5):
  print("***", end=' ')
  print(" ")

print("------------------------")
# S
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range(1,n-2):
  print("*",end=' ')
print(" ")
for i in range(1,n-2):
  print("*",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")

print("      * *")
print("      * *")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
print("------------------------")
# H
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range (1,n+1):
  print("*",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
for i in range (1,n-3):
  print("* *   * *",end=' ')
print(" ")
print("------------------------")

