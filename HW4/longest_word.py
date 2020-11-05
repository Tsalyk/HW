user_str = input("Enter: ")
longest_word = ""

max_len = max(len(i) for i in user_str.split())

for j in user_str.split():
    if len(j) == max_len:
        longest_word += j

print("Amount of words in the string =", len(user_str.split()))
print(f"Longest word:, {longest_word}. It's {max_len} letters long.")
