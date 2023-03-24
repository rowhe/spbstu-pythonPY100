for tuple_ in enumerate(["а", "б", "в"], start = 3):  # перебираем кортежи с индексом и значением
    print(tuple_)

for pos, value in enumerate("абв", start=111):  # start по умолчанию равен 0, но можно задать произвольный
    print("Позиция:", pos, "->", "Значение:", value)
