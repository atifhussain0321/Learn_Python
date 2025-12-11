# Reversing Numbers
num = int(input("Enter a Number: "))
ans = ""

while num > 0:
    ans += str(num % 10)
    num //= 10

print(ans)