"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) телефоны владельцев,
    чьи имена начинаются на букву "м" либо заканчиваются на "а"
    (регистр не имеет значения).
    Перед записью в файл привести номер к формату +380501234567.
"""
from re import sub

def rewrite_phone(read_file, write_file):
    with open(read_file, "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    for k in range(len(lines)):
        find_space = lines[k].find(" ")
        lines[k] = lines[k][:find_space+1] \
        + sub(r"\D", "", lines[k][find_space:])
        find_space = lines[k].find(" ")

        if len(lines[k][find_space+1:]) == 9:
            lines[k] = lines[k].replace(" ", " +380")
        elif len(lines[k][find_space+1:]) == 10:
            lines[k] = lines[k].replace(" ", " +38")
        elif len(lines[k][find_space+1:]) == 11:
            lines[k] = lines[k].replace(" ", " +3")
        elif len(lines[k][find_space+1:]) == 12:
            lines[k] = lines[k].replace(" ", " +")

    new_line = ""
    with open(write_file, "w") as f:
        for index in range(len(lines)):
            find_space = lines[index].find(" ")
            if (lines[index].startswith("М") or
            lines[index].startswith("М") or
            lines[index][:find_space].endswith("А") or
            lines[index][:find_space].endswith("а")):
                new_line += lines[index] + "\n"
        f.write(new_line)
