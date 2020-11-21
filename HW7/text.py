"""
    Дан файл с текстом (text.txt).
    Создать новый файл (edited_text.txt), каждая строка которого получается из
    соответствующей строки исходного файла с обратным порядком слов, причем
    первое слово с заглавной буквы, а все остальные со строчной.
    Например 1 файл содержит:
    Hello world
    How are you
    Тогда второй файл будет содержать:
    World hello
    You are how
"""

def file_to_write(read_file: str, write_file: str) -> None:
    new_line = ""
 
    with open(read_file, "r") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            split_lines = lines[i].split()
            last_symb = split_lines[-1][-1]
            split_lines.reverse()
            split_lines[0].lower()
            full_line = " ".join(split_lines) + last_symb
            full_line = full_line.capitalize().replace(last_symb, "", 1)
            if i != len(lines) -1: 
                new_line += full_line + "\n"
            else: 
                new_line += full_line

    with open(write_file, "w") as f:
        f.write(new_line)
file_to_write("text.txt", "edited_text.txt")