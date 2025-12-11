# Checking that the String is Palindrome or Not 

def pallindrome(text):
    a = ""
    for i in range(len(text)-1,-1,-1):
        a += text[i]
    if a == text:
        print(f"Its a Palindrome")
    else:
        print("Its not a Palindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")