# Check wheater the List is Sortedt or Not

nums = []
index = int(input("How many numbers did you want to add: "))

while index > 0:
    nums.append(int(input("Enter any Positive & Negative Number:- ")))
    index -= 1

for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        continue
    else:
        print("You List is not sorted")
        break
else:
    print("Your List is Sorted")
