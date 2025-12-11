# Seperate Digits
num = int(input("Enter a Number: "))


while num > 0:
    print(num % 10)
    num //= 10

