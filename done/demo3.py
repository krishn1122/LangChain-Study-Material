import random

x = random.randint(1, 100)
count = 1
print("Guess the number between 1 to 100: ")
a = -1

while a != x:
    a = int(input("Enter the number: "))
    if a > x:
        print("Smaller PLease!")
        count += 1
    elif a < x:
        print("Greater number please: ")
        count += 1
print(f"You won the game in {count} attempts and the number was {x}.")
