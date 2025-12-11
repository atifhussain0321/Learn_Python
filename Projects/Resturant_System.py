# Resturant Managment System 
print("Welcome to Annapurna Resturant")

veg_nonveg = input("Are You a Vegetarian, Non-Vegetarian or Both[V/N/B]: ")

veg_items = ['', "Veg Biryani", "Steam Momos", "Fried Momos"]
nonveg_items = []

def veg():
    print(f'''This is the Menu:''')
    num = 1
    for i in range(1,len(veg_items),1):
        print(f"{num}. {veg_items[i]}")
        num += 1
    order_items = []
    def statement(): 
        print("What would You Like to Order?")
        order = int(input("Enter the Serial Number of the Item which You Like to Order: "))
        for i in range(order): #May be Error
            order_items.append(veg_items[i])  #May Be Error
    statement()
    confirm = input(f'You"re order is {print(order_items)} Enter Y/N: ')
    if confirm == "Y" or confirm == "y":
        print("Ok, We have Started Preparing You're Order. It might take around 25-30m")
    else:
        statement()

if veg_nonveg == "V" or veg_nonveg == "v":
    veg()
elif veg_nonveg == "N" or veg_nonveg == "n":
    non_veg()
else:
    both()

