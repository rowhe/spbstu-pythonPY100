BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100 # TODO ввести количество страниц
lines = 50  # TODO ввести количество строк
chars = 25  # TODO ввести количество символов в строке

total_chars = chars * lines * pages  # TODO общее количество символов в книге
total_bytes = total_chars  # TODO размер одной книги в байтах

disk_size = 1.44*1024*1024//total_bytes  # TODO размер дискеты в байтах

print(disk_size)  # TODO найти количество книг, которое поместится на дискете
