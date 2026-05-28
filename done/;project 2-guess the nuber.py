import random
n=random.randint(1,100)
print("**Guess the number between 1 to 100 **")
a=-1
guess=1
while(a!=n):
    a=int(input("Enter the number:"))
    if(a>n):
        print("Smaller number please!")
    elif(a<n):
        print("Greater number please!")
    guess+=1
print(f"You won the game in {guess} attempts and the number was {n}")
