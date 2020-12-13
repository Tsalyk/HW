from random import randint, choice, sample
from string import (ascii_letters, ascii_lowercase, digits, punctuation,
ascii_uppercase)

def password_gen(password_type: int) -> str:
    password = ""
    tmp = ascii_letters + digits

    if password_type == 1:
        while len(password) != 8:
            password += choice(ascii_lowercase)
    elif password_type == 2:
        while len(password) != 8:
            password += choice(tmp)
    elif password_type == 3:
        randlen = randint(8, 16)
        tmp += punctuation
        password += (str(randint(0, 9)) + choice(ascii_uppercase)
        + choice(ascii_lowercase) + choice(punctuation))

        while len(password) != randlen:
            password += choice(tmp)
        password = "".join(sample(password, len(password)))
    return password