"""
    Напишите функцию, которая приинимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""
from string import punctuation


def most_common_word(text: str) -> str:
    words_dict = {}
    text = text.lower()

    for i in text:
        if i in punctuation:
            text = text.replace(i, "")

    words_list = text.split()
    for word in words_list:
        if words_list.count(word) not in words_dict:
            words_dict[words_list.count(word)] = [word]
        else:
            if word not in words_dict[words_list.count(word)]:
                words_dict[words_list.count(word)].append(word)
    sorted_keys = sorted(words_dict)
    words_dict[sorted_keys[-1]].sort()
    return words_dict[sorted_keys[-1]][0]

t_1 = 'Hello, hello world!'
assert most_common_word(t_1) == 'hello'

t_2 = 'Good day! Good day!'
assert most_common_word(t_2) == 'day'

t_3 = 'some text'
assert most_common_word(t_3) == 'some'