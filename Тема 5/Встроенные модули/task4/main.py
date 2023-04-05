# TODO написать функцию, которая выдает трехзначное число
from random import randint

def random_num()-> int:
    random_digit = [randint(0,9) for _ in range(3)]
    str_ = ''.join([str(digit) for digit in random_digit])
    return int(str_)

print(random_num())