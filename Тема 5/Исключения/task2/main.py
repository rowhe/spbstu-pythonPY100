def is_lucky_number(num: int) -> bool:
    ...  # TODO проверить что число шестизначное и положительное
    if num <=0:
        raise ValueError("Число отрицательное")
    if len(str(num)) != 6:
        raise ValueError("В числе меньше 6 чифр")
    ...  # TODO проверить счастливое число или нет
    list_ = [int(d) for d in str(num)]
    bool_ = (sum(list_[:3]) == sum(list_[3:]))
    return bool_

print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
