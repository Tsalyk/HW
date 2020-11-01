import random

print("Hello! Let's play a game. Try to guess a number between 1 and 100 :)")
print("Enter: ", end="")

try:
    random_number = random.randint(1, 10)
    user_input = int(input())
    tries = 1

    while user_input != random_number:
        if user_input > random_number:
            print(f"{user_input} --> try lower :)")

            tries += 1
            user_input = int(input())
        else:
            print(f"{user_input} --> try upper :)")

            tries += 1
            user_input = int(input())
    else:
        print(f"{user_input} -- correct number. Congratulations! You guess it by {tries} attempt. Do you want to continue? (yes/no)")
        user_continue_input = str(input())

        while user_continue_input == "yes":
            print("Enter: ", end="")

            user_input_next = int(input())
            new_tries = 1
            random_number_next = random.randint(1, 10)

            while user_input_next != random_number_next:
                if user_input_next > random_number_next:
                    print(f"{user_input_next} --> try lower :)")

                    new_tries += 1
                    user_input_next = int(input())
                else:
                    print(f"{user_input_next} --> try upper :)")

                    new_tries += 1
                    user_input_next = int(input())
            else:
                print(f"{user_input_next} -- correct number. Congratulations! You guess it by {new_tries} attempt. Do you want to continue? (yes/no)")
                user_continue_input = str(input())
        else:
            print("Thank you for a game. Come back soon :)")
except ValueError:
    print("You entered wrong value.")
