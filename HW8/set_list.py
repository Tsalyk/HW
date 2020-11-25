"""
    Реализовать функции, которые принимают 2 списка чисел и:
    1 функция
    Возвращает список чисел (в порядке возрастания),
    которые содержатся в первом и втором списке одновременно.
    2 функция
    Возвращает список чисел (в порядке убывания),
    которые не содержатся в первом и втором списке одновременно.
    3 функция
    Возвращает количество уникальных чисел,
    которые содержатся во втором списке, но не содержатся в первом.
"""

def get_intersection(first_list: list, second_list: list) -> list:
    interset = set(first_list).intersection(set(second_list))
    return sorted(list(interset))

def get_symmetric_difference(first_list: list, second_list: list) -> list:
    symm_dif = set(first_list).symmetric_difference(set(second_list))
    return sorted(list(symm_dif), reverse=True)

def get_difference(first_list: list, second_list: list) -> list:
    return list(set(second_list).difference(set(first_list)))
