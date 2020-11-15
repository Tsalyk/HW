"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно (не влияет на оценку):
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""
from random import randint, choice, sample
from string import (ascii_letters, ascii_lowercase, digits, punctuation,
ascii_uppercase)

print("Choose password type:\n1) easy password\n2) normall \
password\n3) hard password\n4) your variant of pass")

password_type = int(input("Enter: "))
while 4 < password_type or password_type < 1:
    password_type = int(input("Please, enter a correct type: "))

run = True

if password_type != 4: 
    answer = input("Do you want to choose password length? (y/n)\n")
    if answer == "y":
        user_len = int(input("Enter password length: "))
        if user_len > 8:
            run = False
        while run:
            again_answer = input("It is very unreliable password, do you \
want to continue? (y/n)\n")
            if again_answer == "y":
                run = False
            else:
                user_len = int(input("Enter new length: "))
                if user_len < 8:
                    run = True
                else:
                    run = False

def password_gen(password_type: int) -> str:
    global user_len
    global answer

    password = ""
    tmp = ascii_letters + digits
    try:
        if answer != "y":
            if password_type == 1:
                while len(password) != 8:
                    password += choice(ascii_lowercase)
            elif password_type == 2:
                while len(password) != 8:
                    password += choice(tmp)
            elif password_type == 3:
                randlen = randint(8, 16)
                tmp += punctuation
                password += (str(randint(0, 9)) + choice(ascii_uppercase)
                + choice(ascii_lowercase) + choice(punctuation))

                while len(password) != randlen:
                    password += choice(tmp)
                password = "".join(sample(password, len(password)))
        else:
            if password_type == 1:
                while len(password) != user_len:
                    password += choice(ascii_lowercase)
            elif password_type == 2:
                while len(password) != user_len:
                    password += choice(tmp)
            elif password_type == 3:
                tmp += punctuation
                password += (str(randint(0, 9)) + choice(ascii_uppercase)
                + choice(ascii_lowercase) + choice(punctuation))

                while len(password) != user_len:
                    password += choice(tmp)
                password = "".join(sample(password, len(password)))
    except NameError:
        user_symbols = input("Enter password symbols: ")
        user_len = int(input("Enter password length: "))

        while len(password) != user_len:
            rand_choice = choice(user_symbols)
            if rand_choice != " ":
                password += rand_choice
    return password