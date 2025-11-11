# Print Sum of All Even and Odd till Nth Term
num = int(input("Enter a Number: "))
even = 0
odd = 0
for i in range(1,num+1,1):
    if i%2 == 0:
        even += i
    elif i%2 != 0:
        odd += i
    
print(f'''There are the Following Numbers of Sum in From 1 to {num}:
      Odd: {odd}
      Even: {even}''')
