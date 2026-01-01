try:
    x = int(input("What's your x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")