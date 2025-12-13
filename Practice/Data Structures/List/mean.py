# To Find mean of the List Number
nums = []
index = int(input("How many numbers did you want to add: "))

while index > 0:
    nums.append(int(input("Enter any Positive & Negative Number:- ")))
    index -= 1
sum_ob = 0
idx = 0
for i in nums:
    sum_ob += i
    idx += 1

print(f"Mean value of the given List is {sum_ob//idx}")