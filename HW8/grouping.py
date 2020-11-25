"""
    Пользователь вводит количество групп n.
    Далее вводится n строк, каждая строка начинается с названия группы,
    а затем через пробел идут элементы группы.
    1. Обработать строки и вывести на экран словарь, в котором
    ключи - это группы, а значения - списки элементов групп.
    2. Создать и вывести второй словарь, в котором
    ключи - элементы групп, а зачения - группы.
    Используйте функции!
    Например:
    [out] Введите кол-во групп:
    [in]  2
    [out] 1 группа:
    [in]  fruits apple banana mango kiwi lemon
    [out] 2 группа:
    [in]  citrus lime lemon orange
    [out] {
        'fruits': ['apple', 'banana', 'mango', 'kiwi', 'lemon'],
        'citrus': ['lime', 'lemon', 'orange']
    }
    [out] {
        'apple': ['fruits'],
        'lemon': ['citrus', 'fruits'],
        ...
    }
"""

def group_dict() -> dict:
    try:
        group_num = int(input("Enter groups number: "))
    except ValueError:
        group_num = int(input("Please, enter an integer: "))

    i = 0
    items_list = []

    while i != group_num:
        items_input = input(f"{i+1} group:\n")
        items_input = items_input.split()
        items_list.append(items_input)
        i += 1
    items_dict = {}

    for ind in range(len(items_list)):
        items_dict[items_list[ind][0]] = [i for i in items_list[ind][1:]]

    print(items_dict)
    return element_dict(items_dict)


def element_dict(items_dict: dict) -> dict:
    new_dict = {}

    for key, value in items_dict.items():
        for ind in range(len(value)):
            if value[ind] not in new_dict:
                if value[ind] in items_dict[key]:
                    new_dict[value[ind]] = [key]
            else:
                if value[ind] in items_dict[key]:
                    new_dict[value[ind]].append(key)
    return new_dict
print(group_dict())
