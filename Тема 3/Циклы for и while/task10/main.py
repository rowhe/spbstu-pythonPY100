list_ = [3, 4, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# завести отдельные счетчики для четных и нечетных чисел
counter_odd = 0
counter_even = 0

# с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

for i in list_:
    if i % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1

# print(counter_even)
# print(counter_odd)

# вывести каких чисел больше
if counter_even == counter_odd:
    print("Четных и нечетных одинаковое количество")
elif counter_even < counter_odd:
    print("Нечетных чисел больше")
else:
    print("Четных чисел больше")
