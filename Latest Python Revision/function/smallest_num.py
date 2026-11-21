def smallest(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        print("Smaller value:", num1)

    elif num2 < num1 and num2 < num3:
        print("Smaller value:", num2)

    else:
        print("Smaller value:", num3)
smallest(40, 30, 80)
