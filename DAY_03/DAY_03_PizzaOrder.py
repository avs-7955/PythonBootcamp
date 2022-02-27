print("Welcome to Python Pizza Deliveries!")

size = input("What side pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y or N.\n")
extra_cheese = input("Do you want extra cheese? Y or N.\n")

# COST
# SMALL PIZZA = $15
# MEDIUM PIZZA = $20
# LARGE PIZZA = $25

# PEPPERONI FOR SMALL PIZZA = $2
# PEPPERONI FOR MEDIUM AND LARGE PIZZA = $3

# EXTRA CHEESE FOR ANY SIZE PIZZA = $1

if(size == "S"):
    cost = 15
elif(size == "M"):
    cost = 20
else:
    cost = 25

if(extra_cheese == "Y"):
    cost += 1

if(add_pepperoni == "Y"):
    if(size == "S"):
        cost += 2
    else:
        cost += 3

print(f"The cost of your pizza is ${cost}.Happy Eating!")
