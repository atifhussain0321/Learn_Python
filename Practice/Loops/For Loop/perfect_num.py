# To Check that the Num is a Perfect Number
num = int(input("Enter a Number: "))
ans = 0

for i in range(1,num,1):
    if num % i == 0:
        ans += i

if ans == num:
    print(f'Its a Perfect Number {ans}')
else:
    print(f"Its not a Perfect Number: {num}")