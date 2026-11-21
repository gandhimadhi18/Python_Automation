def larger(num):
    larger = num[0]
    for i in range(0, len(num)):
            if num[i] > larger:
                larger = num[i]
    print(larger)
larger([20, 5, 50, 0, 80, 10, 100, -5])