import time
import sys

# Function to print text slowly like typing
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline at the end

# Welcoming part
slow_print("Welcome to Python's cafeteria.")
slow_print("I'm Barista, the waiter of this cafeteria.\n")
time.sleep(1)

# Name request for the client
name = input("What should I call you?\n")
time.sleep(0.5)

# In case that SALAH came here
if name.lower() == '>salah':
    evil = input("\nAre you evil? YES/NO ")
    time.sleep(0.5)

    if evil.lower() == 'yes':
        slow_print("\nWe have nothing for you here.", 0.05)
        exit()

    elif evil.lower() == 'no':
        slow_print("\nOh, I thought that you were the EVIL-SALAH, you are welcome sir\n", 0.05)
    
else:
    slow_print(f"\nYou are most welcome, my dear {name.upper()}.\n", 0.04)
    time.sleep(0.5)

# The menu part
menu = ("Coffee, Milk, Cappuccino, Latte, Ice Tea\n")
slow_print("Here's our menu:")
slow_print(menu)
order = input("What would you like to order?\n").lower()
time.sleep(0.5)

if order in ['coffee', 'milk', 'cappuccino', 'latte', 'ice tea']:
    slow_print("Great choice!\n", 0.04)
else:
    slow_print(f"\nSorry {name.upper()} we don't have {order.upper()}\n", 0.04)
    sec_order = input(f"Do you want something of these? : YES/NO\n{menu}")    
    if sec_order.lower() == 'yes':
        order = input("\nGreat, what do you want to order? ")
    elif sec_order.lower() == 'no':
        slow_print("\nThank you for your visit!", 0.04)
        exit()

print()
slow_print(f"How many {order.upper()}s would you like?\n1, 2, 3,... ")
quantity = int(input(""))
print()

# Wait please
slow_print(f"{name.upper()}, your {quantity} {order.upper()}(s) is being prepared.\n", 0.04)
time.sleep(1)
slow_print("It will be ready shortly!\n", 0.04)
time.sleep(1)

slow_print(f"{name.upper()}, we hope that you have enjoyed your {order.upper()}\n", 0.04)
slow_print("Now here's the bill :\n", 0.04)
time.sleep(1)

# Pricing
if order.lower() == 'coffee':
    price = 2
elif order.lower() == 'milk':
    price = 1
elif order.lower() == 'cappuccino':
    price = 3
elif order.lower() == 'latte':
    price = 3
elif order.lower() == 'ice tea':
    price = 1
else:
    price = 0

bill = quantity * price

# Print bill
slow_print("------------------------------------------", 0.002)
slow_print("|                                        |", 0.002)
slow_print("|               YOUR BILL                |", 0.004)
slow_print("|                                        |", 0.002)
slow_print("|  Order        Price   Quantity   Total |", 0.004)
slow_print(f"|  {order:<12} {price:<2}$      {quantity:<8} {bill:<6}$ |", 0.004)
slow_print("|                                        |", 0.002)
slow_print("|          THANK YOU, COME AGAIN! :)     |", 0.004)
slow_print("|                                        |", 0.002)
slow_print("------------------------------------------", 0.002)
