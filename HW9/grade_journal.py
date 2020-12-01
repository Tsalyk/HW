"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.
    Программа выводит список фамилий, отсортированный по их баллам по убыванию.
    Пример:
    [out] Введите количество студентов:
    [in]  3
    [out] Введите фамилию и балл:
    [in]  Иванов 87
    [out] Введите фамилию и балл:
    [in]  Смирнов 90
    [out] Введите фамилию и балл:
    [in]  Фролов 89
    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""
def main():
    users_list = get_user_input()
    new_lst = sort_users(users_list)

    for ind, el in enumerate(new_lst):
        print(f"{ind+1}. {el[:el.find(' ')]}")

def get_user_input() -> list:
    num_students = int(input("Enter number of students: "))
    students_list = []

    while len(students_list) != num_students:
        student_mark = input("Enter a surname and a mark:\n")
        students_list.append(student_mark)
    return students_list

def sort_users(some_lst: list) -> list:
    some_lst = sorted(some_lst, key=lambda x: x[-2:], reverse=True)
    return some_lst

main()