# Check Eligiblity of Voter Id Card

name = input("Enter Your Name: ")
age = int(input("Enter You Age: "))
gen = input("Enter Your Gender[M/F/T]: ")
address = input("Enter Your Address: ")

if len(name) >= 4 and age >= 18 and (gen == "M" or gen == "F" or gen == "T") and len(address) >= 10:
    print(f"\nDear {name}, You're Eligible For Voter Card")
else:
    print("You're Not Eligible For Voter Card")
    print('''
    Criteria: 
          1. Minimum 4 Characters of Name
          2. 18+
          3. Male, Female or Transgender
          4. Minimum 10 Chaarcters of Address
''')

print("Thank You")