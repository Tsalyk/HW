"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
        Программа выводит сообщение:
        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********
"""
from string import punctuation

def main() -> str:
    password = input_password()
    confirm_pass = str(input("Confirm your password: "))

    while confirm_pass != password:
        password = input_password()
        confirm_pass = str(input("Confirm your password: "))
    phone = input_phone()
    email = input_email()
    pass_star = len(confirm_pass) * "*"

    print(
    f"Congratulations on successful registration!\nYour phone \
number: {phone}\nYour email: {email}\nYour password: {pass_star}"
)

def input_phone() -> str:
    phone_num = str(input("Enter phone number: "))
    valid_phone = ""

    for digit in phone_num:
        if digit.isdigit():
            valid_phone += digit

    if valid_phone.startswith("38") and len(valid_phone) == 12:
        return "+" + valid_phone
    elif valid_phone.startswith("0") and len(valid_phone) == 10:
        return "+38" + valid_phone
    else:
        print("Please, enter valid phone number!")
        input_phone()

def input_email() -> str:
    user_email = str(input("Enter email: "))
    if len(user_email) >= 6 and user_email.count("@") == 1:
        dog_index = user_email.find("@")
        counter = 0
        for i in user_email[dog_index:]:
            if i.isdigit():
                counter += 1
        if (user_email[dog_index:].count(".") == 1 and counter == 0 and not
        user_email.endswith(".")):
            return user_email
        else:
            print("Please, enter correct email!")
            return input_email()
    else:
        print("Please, enter correct email!")
        return input_email()

def input_password() -> str:
    user_pass = str(input("Enter password: "))
    counter_upper = 0
    counter_lower = 0
    counter_digit = 0
    counter_punctuation = 0
    counter_space = 0

    for symbol in user_pass:
        if symbol.isupper():
            counter_upper += 1
        elif symbol.islower():
            counter_lower += 1
        elif symbol.isdigit():
            counter_digit += 1
        elif symbol in punctuation:
            counter_punctuation += 1
        elif symbol.isspace():
            counter_space += 1

    if (len(user_pass) >= 8 and counter_upper >= 1 and counter_lower >= 1 and
    counter_digit >= 1 and counter_punctuation >= 1 and counter_space == 0):
        return user_pass
    else:
        print("Please, enter correct password!")
        return input_password()
