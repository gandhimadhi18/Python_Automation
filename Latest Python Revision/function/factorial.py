def factorial(num):
    fact = 1
    # start, stop value. doesn't include stop value
    for i in range(1, num +1):
        fact = fact * i
        print("Factorial of", i, "is:", fact)

factorial(5)
