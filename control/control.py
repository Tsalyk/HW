# 1. Создайте переменную x, которая равняется 2 в степени 3


# 2. Прибавьте к x 3


# 3. Сгенерируйте список num_list длиной x, из случайных чисел в диапазоне от 1 до x


# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел


# 5. Вставьте в средину списка число 11.


# 6. Запишите в файл list_info.txt строчки
#    - количество элементом списка
#    - количество уникальных элементов списка
#    - самое маленькое число списка
#    - сумму чисел списка кратных 3


# 7. Создайте список countries_info из 3 словарей c ключами
#    'country', 'population', 'cities' и заполните их любыми значениями
#    ('country' - строка, 'population' - число, 'cities' - список строк)


# 8. Отсортируйте в каждом словаре cities по длине строк в порядке убывания


# 9. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания


# 10. Напишите функцию create_country_info, которая принимает 3 параметра
#     country, population и cities
#     и возвращает словарь типа
#     {'country': 'USA', 'population': 123, 'cities': ['New York', 'Los Angeles', 'Portland']}


# 11. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info


# 12. Запуште код в репозиторий (существующий либо новый),
#     ссылку на файл прикрепите к 10 дз

# 1 
x = 2 ** 3

# 2
x += 3

# 3
from random import randint

num_list = []
while len(num_list) != x:
    num_list.append(randint(1, x))

# 4
reversed_list = reversed(num_list)

for num in reversed_list:
    print(num, end=" ")
print()

# 5
num_list.insert(len(num_list)//2, 11)
print(num_list)

# 6
# with open("list_info.txt", "a") as f:
#     f.write(str(len(num_list)) + "\n")
#     f.write(str(len(set(num_list))) + "\n")
#     f.write(str(min(num_list)) + "\n")
#     f.write(str(sum([i for i in num_list if i / 3 == 0])) + "\n")

# 7
countries_info = [
{"country": "Ukraine", "population": 5000000,
"cities": ["Lviv", "Kiev", "Kharkiv"]}, {"country": "America", "population": 9000000,
"cities": ["London", "New-Your", "Los-Angelos"]}, {"country": "Amsterdam", "population": 8000000,
"cities": ["Some city", "Another city", "Space"]}
]

# 8
for dct in countries_info:
    dct['cities'].sort(key=len, reverse=True)

# 9
for dct in countries_info:
    dct["cities"].sort(key=len)


# 10
def create_country_info(country, population, cities):
    data_dict = {
    "country": country, "population": population,"cities": cities
    }
    return data_dict


# 11
data = create_country_info("USA", 123, ['New York', 'Los Angeles', 'Portland'])
countries_info.insert(0, data)
