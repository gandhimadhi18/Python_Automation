def fibonacci(num):
    first =0
    second = 1

    print(first)
    print(second)

    for i in range(1, num - 1):
        next = first + second
        first = second
        second = next
        print(next)
fibonacci(5)
