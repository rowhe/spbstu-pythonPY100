# TODO реализовать функцию
def get_unique_words(str_):
    a = str_.split()
    uniq = set(a)
    uniq_list = list(uniq)
    uniq_list.sort()
    return uniq_list


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
