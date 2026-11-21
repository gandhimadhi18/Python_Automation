def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(10, 5)
print("Area value:", result)

result = calculate_area(20, 4)
print("Area value:", result)

result = calculate_area(15, 3)
print("Area value:", result)
# result is used to reuse the calculate area
print("Double area:", result * 2)
print("Trible area:", result * 3)