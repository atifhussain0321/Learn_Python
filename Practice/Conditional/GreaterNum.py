# Greater Question
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

if a > b:
    print(f'{a} is Greater than {b}')
elif a < b:
    print(f'{b} is Greater than {a}')
else:
    print("Error" *100)