def is_palindrome(str_):
    check = ''.join(str_.lower().split())
    if check == check[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


is_palindrome("Кит на море не романтик")
is_palindrome("Прочая строка")
