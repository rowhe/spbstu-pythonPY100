# Пусть функция принимает два числа, складывает их и возвращает результат
def add_func(a: int, b: int) -> int:
    # a и b аргументы, которые принимает функция
    # эти аргументы будут не доступны вне тела функции
    add = a + b

    # чтобы вернуть результат нужно использовать ключевое слово return
    return add


def empty_func():  # функция без аргументов и возвращаемых результатов
    ...


result = add_func(5, 10)  # сохраняем результат функции в переменную
print(result)  # 15

print(empty_func())  # None
