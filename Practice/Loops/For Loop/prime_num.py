#  To Check Wheather the Number is a Prime Number or Not
num = int(input("Enter a Number: "))
sum = 0
count = 0
for i in range(1,num +1, 1):
    if num % i == 0:
        sum += i
        count += 1

if sum == num + 1 and count == 2:
    print(f"{num} is a Prime Number")
else: 
    print(f"{num} is not a Prime Number")

