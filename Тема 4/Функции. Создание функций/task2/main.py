def pow_func(base, pow_=2):
    print(base, "**", pow_)


# по умолчанию возводим число в степень два
pow_func(4,3)  # 4 ** 2

# переопределяем аргумент по умолчанию
pow_func(3, pow_=3)  # 3 ** 3

# опять умолчанию возводим число в степень два
pow_func(5)  # 5 ** 2

# переопределяем аргумент по умолчанию
pow_func(3, pow_=3)  # 3 ** 3

# используем позиционные аргументы
pow_func(2, 5)  # 2 ** 5

# используем именованные аргументы
pow_func(pow_=2, base=8)  # 8 ** 2
