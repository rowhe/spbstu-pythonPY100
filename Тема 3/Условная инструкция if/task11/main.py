month = 9

spring_months = [3, 4, 5]  # TODO записать словарь весенних месяцев, где ключ это номер месяца, а значение его название
summer_months = [6, 7, 8]  # TODO записать список месяцев лета
autumn_months = [9, 10, 11]  # TODO записать кортеж месяцев осени
winter_months = [12, 1, 2]  # TODO записать список месяцев зимы

if month in spring_months:
    print("Весна")
elif month in summer_months:
    print("Лето")
# TODO дописать условие elif для осени и зимы
elif month in winter_months:
    print("Зима")
elif month in autumn_months:
    print("Осень")
