# TODO заполнить список случайными числами
from random import randint
# TODO посчитать количество отрицательных чисел
list_= [randint(-100, 100) for _ in range(50)]
list_2 = [negative for negative in list_ if negative < 0]
print(len(list_2))