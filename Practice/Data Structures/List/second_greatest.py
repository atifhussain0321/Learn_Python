nums = []
index = int(input("How many numbers did you want to add: "))

while index > 0:
    nums.append(int(input("Enter any Positive & Negative Number:- ")))
    index -= 1

g = 0
G = 0

for i in nums:
    if i > G:
        g = G
        G = i

print(f"Second Largest Number is {g} with the Index of {nums.index(g) + 1}")
