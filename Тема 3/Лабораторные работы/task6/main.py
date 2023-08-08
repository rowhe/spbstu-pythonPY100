list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 25, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Оформить решение
list_numbers[-1] = list_numbers.pop(list_numbers.index(max(list_numbers)))
print(list_numbers)
