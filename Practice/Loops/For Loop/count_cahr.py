a = input("Enter a Number: ")

char = 0
digit = 0
spchar = 0

for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        spchar += 1

print(f'''
Your Charcter are:
      {digit} {spchar} {char}
''')
