# To Find Factor of a Number
num = int(input("Enter a Number: "))

for i in range(1,num+1,1):
    if num % i == 0:
        print(i)