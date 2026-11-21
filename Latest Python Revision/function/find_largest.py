def find_largest(a, b, c):
    # a = 20
    # b = 50
    # c = 30
    if a > b and a > c:
        print("A larger")
    elif b > a and b > c:
        print("B is larger")
    else:
        print("c is larger")
find_largest(20, 50 , 30)
