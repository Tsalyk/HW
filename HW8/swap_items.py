"""
    Напишите функцию, которая принимает словарь,
    меняет местами ключи и значения и возвращает его.
    Покройте функцию несколькими тестами.
    Пример:
    a = {'key': 'value', 'd': 1234}
    b = swap_items(a)
    print(b)
    {'value': 'key', 1234: 'd'}
    * пропускайте пары, в которых значение не может быть ключем
    ** ключем словаря может быть только не изменяемый объект,
        а точнее тот, который можно захешировать функцией hash()
"""
def change_dict_items(some_dict: dict) -> dict:
    new_dict = {}
    try:
        for key, value in some_dict.items():
            new_dict[value] = key
    except TypeError as err:
        print(err)
        return some_dict
    return new_dict

t_1 = {'key': 'value', 'd': 1234}
assert change_dict_items(t_1) == {'value': 'key', 1234: 'd'}

t_2 = {'a': 'text', 'b': 'hello'}
assert change_dict_items(t_2) == {'text': 'a', 'hello': 'b'}

t_3 = {'some_key': 'some_value', 'another_key': 'another_value'}
assert change_dict_items(t_3) == {'some_value': 'some_key', 'another_value': 'another_key'}
