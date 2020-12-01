data = [
    (2, 'green'), (1, 'blue'), (2, 'yellow'), (1, 'aquamarine'),
    (4, 'red'), (3, 'gold'), (5, 'black'), (2, 'brown'),
    (5, 'pink'), (1, 'purple'), (4, 'white'), (1, 'gray'),
]

# 1. Выведите отсортированный список data по цвету (2 элемент кортежа).
def color_sort(data: list) -> list:
    data = sorted(data, key=lambda x: x[1])
    return data
print(color_sort(data))

# 2. Отсортируйте список по 1 элементу кортежа, а если значения одинаковые,
#    то их отсортировать по 2 элементу. Результат выведите на экран.
def digit_sort(data: list) -> list:
    data = sorted(data, key=lambda x: x[0])
    data_dict = {}
    new_data = []

    for i in range(len(data)):
        if data[i][0] not in data_dict:
            data_dict[data[i][0]] = [data[i][1]]
        else:
            data_dict[data[i][0]].append(data[i][1])
    for key, value in data_dict.items():
        for i in range(len(value)):
            new_data.append((key, sorted(value)[i]))
    return new_data
print(digit_sort(data))

# 3. С помощью filter() и lambda выведите только те кортежи из списка,
#    цвет которых состоит из 4 букв.
def four_letters(data: list) -> list:
    return list(filter(lambda x: len(x[1]) == 4, data))
print(four_letters(data))

# 4. Выведите цвет, которой состоит из найбольшего количества букв.
def max_letters(data: list) -> str:
    maxlen = max([len(data[i][1]) for i in range(len(data))])
    for i in range(len(data)):
        if len(data[i][1]) == maxlen:
            return data[i][1]
print(max_letters(data))