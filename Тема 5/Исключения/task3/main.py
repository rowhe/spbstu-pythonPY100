# TODO написать функцию index
def index(list_, value) -> int:
    for i, cur_value in enumerate(list_):
        if cur_value == value:
            return i


list_items = [1, 2, "3", 1]
print(index(list_items, 1) == list_items.index(1))  # True
