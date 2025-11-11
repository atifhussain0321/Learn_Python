# Print Table of Any Number
print("Get Table of Any Number")
num = int(input("Enter Your Number: "))
len = int(input("Enter the Lenght of Table: "))

l = 1
for i in range(num,num * len + 1,num):
    print(f"{num} * {l} = {i}")
    l += 1

print("Thanks 😍")