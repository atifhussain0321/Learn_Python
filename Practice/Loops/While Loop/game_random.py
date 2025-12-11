import random

tries = 0
ans = 0
max = 3

print("Welcome to Random Number Gussing Game:- ")
a = int(input("Enter the number from you want to guess: "))
b = int(input("Enter the number to you want to guess: "))
num = random.randint(a,b)
custom = input("Do you want to customize maximum limit of tries[T/F]: ")

if custom == "T" or custom == "t" or custom == "True" or custom == "true":
    max = int(input("Enter the maximum tries that you want to do: "))

while True:
    ans = int(input("Guess the number that our system generated :- "))
    tries += 1

    if ans == num and tries <= max:
        print(f"Congratulation You gueed true in the {tries} time.")  
        break  
    elif ans > num and tries <= max:
        print(f"Go a little lower, you have only {max - tries} left only")
    elif ans < num and tries <= max:
        print(f"Go a Little higher, you have only {max - tries} left only")
    elif tries > max: 
        print(f"You lost the game, the number was {num}")
        break
        
