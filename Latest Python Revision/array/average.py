def average(num):
    total = 0
    average = 0
    for i in range(0, len(num)):
        total = total + num[i]
        length = len(num)
        average = total/length
        print(average)
average([20, 15, 30, 40, 60])
