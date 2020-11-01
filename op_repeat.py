num = int(input("Enter: "))

new_num = num // 10000 * 10000 + num % 1000
finall_num = new_num // 100 * 100 + new_num % 10

print(finall_num)