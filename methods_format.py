user_str = input("Enter: ")

lower_count = 0
upper_count = 0
lower_contain = ""
upper_contain = ""

for letters in user_str:
    if letters.isupper():
        upper_count += 1
        upper_contain += " " + letters
    elif letters.islower():
        lower_count += 1
        lower_contain += " " + letters

if upper_count > lower_count:
    print(f"1. Started string: '{user_str}'.\nRefreshed string: \
'{upper_contain}'.")
elif lower_count > upper_count:
    print(f"1. Started string: '{user_str}'.\nRefreshed string: \
'{lower_contain}'.")
else:
    print(f"1. Started string: '{user_str}'.\nRefreshed string: \
'{user_str.swapcase()}'.")

counter = 0
new_str = ""

for words in user_str.split():
    if words[0].isupper():
        counter += 1
        if counter == len(user_str.split()):
            new_str = "done: " + user_str
    else:
        new_str = user_str.replace(user_str[:5], "draft: ")

print(f"2. Started string: '{user_str}'.\nRefreshed string: \
'{new_str}'.")

updated_str = ""
if len(user_str) > 20:
    updated_str = user_str[21:]
    print(f"3. Started string: '{user_str}'.\nRefreshed string: \
'{updated_str}'.")
else:
    updated_str = "@" * (20 - len(user_str)) + " " + user_str
    print(f"3. Started string: '{user_str}'.\nRefreshed string: \
'{updated_str}'.")