students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

# TODO посчитать средний возраст
ages = [s["age"] for s in students_list]
middle_age = sum(ages) / len(ages)

print([s for s in students_list if s["age"] < middle_age])

# TODO распечатать список словарей студентов, возраст которых меньше среднего
