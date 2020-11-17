"""
    Выполните все пункты.
    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

f = "file_practice.txt"

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

with open(f, "w") as file:
    file.write("Starting practice with files\n")


# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

with open(f, "r") as file:
    line = file.read()
    print(line)

    with open(f, "r") as file:
        line = file.read(5)
        print(line)


# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

with open("text.txt", "r") as file:
    line = file.read()
    
    if line.count("i") > line.count("e"):
        line = line.replace("i", "e")
    else:
        line = line.replace("e", "i")

    with open(f, "a") as file:
        file.write(f"\n{line}")

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

with open(f, "r") as file:
    line = file.readlines()
    space_ind = line.index("\n")

with open(f, "w") as file:
    line[space_ind] = "*some pasted text*\n"
    file.write("".join(line))

with open(f, "a+") as file:
    file.read()
    if file.tell() % 2 == 0:
        file.write("\the end")
    else:
        file.write("\nbye")
