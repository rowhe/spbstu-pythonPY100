# TODO реализовать функцию
def get_sentences_list(str_):
    list_ = []
    for sent in str_.split('.'):
        if sent:
            list_.append(sent.strip())
    return list_

print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
