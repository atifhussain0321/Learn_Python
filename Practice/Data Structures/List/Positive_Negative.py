# Finding Positive and Negative of a List
 
nums = []
index = int(input("How many numbers did you want to add: "))

while index > 0:
    nums.append(int(input("Enter any Positive & Negative Number:- ")))
    index -= 1

for i in nums:
    if i > 0:
        print(f'{i} is a Positive Number')
    elif i < 0:
        print(f'{i} is a Negative Number')
    else:
        print("Hii I', Zero")
        