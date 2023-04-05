students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

# TODO распечатать с использованием f-строк
for key, value in students_dict.items():
    print(f'Студент {key} получил {value} баллов')
