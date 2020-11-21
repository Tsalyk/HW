"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num: int) -> bool:
    first_num = 0
    second_num = 0
    length = int(len(str(ticket_num))/2)

    for i in str(str(ticket_num)[:length]):
        first_num += int(i)
    for j in str(str(ticket_num)[length:]):
        second_num += int(j)
    return first_num == second_num

assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print('All right!')