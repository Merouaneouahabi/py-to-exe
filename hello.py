# Welcoming part
print("Welcome to Python's cafeteria.\nI'm Barista, the waiter of this cafeteria.\n")

# Name request for the client
name = input("What should I call you?\n")

# In case that SALAH came here
if name.lower() == '>salah':
    evil = input("\nAre you evil? YES/NO ")

    if evil.lower() == 'yes':
        print("\nWe have nothing for you here.")
        exit()

    elif evil.lower() == 'no':
        print("\nOh, I thought that you were the EVIL-SALAH, you are welcome sir\n")
    
else:
    print(f"\nYou are most welcome, my dear {name.upper()}.\n")


# The menu part
menu = ("Coffee, Milk, Cappuccino, Latte, Ice Tea\n")

# The order part
print(f"Here's our menu:\n{menu}\nWhat would you like to order?")
order = input("").lower()
if order in ['coffee', 'milk', 'cappuccino', 'latte', 'ice tea']:
    print("Great choice")
else:
    print(f"\nSorry {name.upper()} we don't have {order.upper()}\n")
    sec_order = input(f"Do you want something of these? : YES/NO\n{menu}")    
    if sec_order.lower() == 'yes':
        order = input("\nGreat, what do you want to order? ")
    elif sec_order.lower() == 'no':
        print("\nThank you for your visit!")
        exit()

print("")

# Task 02: how many coffees you want
print(f"How many {order.upper()}s would you like?\n1, 2, 3,... ")
quantity = int(input(""))
print("")

# Wait please
print(f"{name.upper()}, your {quantity} {order.upper()}(s) is being prepared.\n\nIt will be ready shortly!\n")

print("")
print(f"{name.upper()}, we hope that you have enjoyed your {order.upper()}\n\nNow here's the bill :\n")


#Pricing
if order.lower() == 'coffee':
    price = 2

if order.lower() == 'milk':
    price = 1
    
if order.lower() == 'cappuccino':
    price = 3

if order.lower() == 'latte':
    price = 3

if order.lower() == 'ice tea':
    price = 1

#Bill rules
bill = quantity * price


# Create a simple box with the bill centered and aligned
print("------------------------------------------")
print("|                                        |")
print("|               YOUR BILL                |")
print("|                                        |")
print("|  Order        Price   Quantity   Total |")
print(f"|  {order:<12} {price:<2}$      {quantity:<8} {bill:<6}$ |")
print("|                                        |")
print("|          THANK YOU, COME AGAIN! :)     |")
print("|                                        |")
print("------------------------------------------")
