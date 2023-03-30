# # TODO оформить решение в виде функции
# count_stairs = 4
# for i in range(1, count_stairs + 1):
#     print("*" * i)


# TODO вызвать функцию без аргументов и с аргументом равным 10
def func(n=4):
    for i in range(1, n+1):
        print("*" * i)
func()
func(10)
