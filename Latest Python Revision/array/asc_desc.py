def asc_desc(num):
    # num = [25, 70 , 80, 90, -5, 40, 80]
    for i in range(0, len(num)):
        for j in range(0, len(num)):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp

    print("Ascending order")
    for i in range(0, len(num)):
        print(num[i])

    print("Descnding order")
    for i in range(len(num) -1, -1, -1):
        print(num[i])
asc_desc([25, 70 , 80, 90, -5, 40, 80])