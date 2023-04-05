def task(num: int) -> bool:  # TODO добавить аннотацию типов
    list_ = [int(digit) for digit in str(abs(num)) ]  # TODO найти сумму цифр числа и понять двузначная ли она
    return 10 <= sum(list_) <= 99

print(task(12))
print(task(555))
print(task(-12))
print(task(-149))
