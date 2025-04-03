# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >=120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# guess if even or odd
# number = int(input("type a number I will say if its odd or even: "))

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Your ticket costs $5")
    elif age <= 18:
        print("Your ticket costs $7")
    else:
        print("Your ticket costs $12")
else:
    print("Sorry you have to grow taller before you can ride.")