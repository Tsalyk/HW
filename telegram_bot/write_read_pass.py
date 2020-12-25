def write_pass(password: str) -> None:
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")


def check_pass(password: str) -> bool:
    with open("passwords.txt", "r") as file:
        return password + "\n" in file.readlines()