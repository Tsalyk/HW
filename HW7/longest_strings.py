"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.
    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""


def longest_strings(input_list: list) -> list:
    """ Функция возвращает список самых длинных строк из списка input_list """

    words_length = [len(i) for i in input_list]
    the_longest_words = [w for w in input_list if len(w) == max(words_length)]
    return the_longest_words

t_1 = ['x']
assert longest_strings(t_1) == ['x']

t_2 = ['abc',  'eeee',  'abcd', 'dcd']
assert longest_strings(t_2) == ['eeee', 'abcd']

t_3 = ['a', 'abc', 'cbd', 'zzzzzz', 'a', 'abcdef', 'asasa', 'aaaaaa']
assert longest_strings(t_3) == ['zzzzzz', 'abcdef', 'aaaaaa']

t_4 = ['enyky', 'benyky', 'yely', 'varennyky']
assert longest_strings(t_4) == ['varennyky']

t_5 = ['abacaba', 'abacab', 'abac', 'xxxxxx']
assert longest_strings(t_5) == ['abacaba']

print('All right!')