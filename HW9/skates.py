"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, который не меньше размеров его ноги.
    Напишите программу, которая принимает список доступных размеров коньков и
    список размеров ног желающих.
    И выводит наибольшее количество людей,
    которые смогут покататься одновременно.
    Например:
    [in]
    [39, 38, 41, 37]
    [40, 39, 41]
    [out]
    2
"""

def check_skates(available_skates: list, sizes: list) -> list:
    available_skates.sort()
    sizes.sort()
    deleted_items = []

    for i in available_skates:
        for j in sizes:
            if i >= j:
                deleted_items.append(j)
                sizes.remove(j)
                available_skates.remove(i)
                available_skates.insert(0, 0)
                break
    return len(deleted_items)
print(check_skates([39, 38, 41, 37], [40, 39, 41]))