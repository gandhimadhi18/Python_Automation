def smaller(num):
    smaller = num[0]
    for i in range(0, len(num)):
        if num[i] < smaller:
            smaller = num[i]
    print(num[i])
smaller([20, 5, 50, 0, 80, 10, 100, -5])