# Checking that the Number is Palandroimic or not

num = int(input("Enter a number: "))
p = num
rev = 0

while num > 0:
    rev = rev *10 + num % 10
    num //= 10

if int(rev) == p:
    print("True, Its a Palandromic Number.")
else:
    print("False, NOOOOOOOOO")