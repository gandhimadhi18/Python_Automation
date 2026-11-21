# numbers =[1, 2, 3, 4, 5]
# squares =[]
# for number in numbers:
#     squares.append(number * number)
#     print(squares)

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)