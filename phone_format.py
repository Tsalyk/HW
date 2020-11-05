user_number = input("Enter: ")
phone_number = ""

for digits in user_number:
    if digits.isnumeric():
        phone_number += digits

while len(phone_number) != 10 and len(phone_number) < 12:
    print("Please, enter correct number:", end=" ")
    user_number = input()
    phone_number = ""

    for digits in user_number:
        if digits.isnumeric():
            phone_number += digits
else:
    print(phone_number)