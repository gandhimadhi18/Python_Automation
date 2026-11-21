def second_larger(num):
    for i in range(0, len(num)):
        for j in range(i+1, len(num)):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp

    first = num[0]
    second = num[1]

    print("Largest:", first)
    print("Second largest:", second)
second_larger([20, 5, 50, 0, 80, 10, 100, -5])