def factorial(a: int) -> int:
    result = 1
    for num in range(1, a+1):
        result *= num
    return result


print(factorial(5))  # TODO распечатать результат выполнения функции factorial от числа 5
