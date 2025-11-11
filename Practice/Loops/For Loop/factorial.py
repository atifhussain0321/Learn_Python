# Factorial of a Number
num = int(input("Enter a Number: "))
ans = 1
for i in range(1,num+1,1):
    ans *= i
print(f'Factorial of {num} is {ans}')