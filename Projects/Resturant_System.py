# Resturant Managment System 
print("Welcome to Annapurna Resturant")

veg_nonveg = input("Are You a Vegetarian, Non-Vegetarian or Both[V/N/B]: ")

veg_items = ['Chowmein', "Veg Biryani", "Steam Momos", "Fried Momos"]
nonveg_items = []

def veg():
    print(f'''This is the Menu:''')
    num = 1
    for i in range(1,len(veg_items),1):
        print(f"{num}. {veg_items[i]}")
        num += 1
    print("What would You Like to Order?")
    order = int(input("Enter the Serial Number of the Item which You Like to Order: "))
    order_items = []
    for i in range(order): #May be Error
        order_items.add(veg[i])  #May Be Error
    print("")

if veg_nonveg == "V" or veg_nonveg == "v":
    veg()
elif veg_nonveg == "N" or veg_nonveg == "n":
    non_veg()
else:
    both()

