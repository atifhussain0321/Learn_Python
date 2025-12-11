import random

tries = 0
ans = 0

print("Welcome to Random Number Gussing Game:- ")
a1 = int(input("Enter the First Number From that Your will start gueeing: "))
a2 = int(input("Enter the Last Number From that Your will end gueeing: "))
a3 = int(input("Enter the maximum time in which you wanna to try: "))

num = random.randint(a1,a2)

while num != ans:
    ans = int(input("Guess the Number that our system generated: "))
    tries += 1
    if tries >= a3: 
        print("Your lost the game, sorry restart the progam and try again!!")
        print(f"Number was {num}")
        break

if tries < a3:
    print("Cogratulation, You Done it in " + str(tries) + " time")
