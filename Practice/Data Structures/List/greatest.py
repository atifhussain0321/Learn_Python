# To Find Greatest in the List
nums = []
index = int(input("How many numbers did you want to add: "))

while index > 0:
    nums.append(int(input("Enter any Positive & Negative Number:- ")))
    index -= 1

greatest = 0
for i in nums:
    if i > greatest:
        greatest = i
    
print(f'Greatest number is {greatest} and its index is {nums.index(greatest) + 1}')
