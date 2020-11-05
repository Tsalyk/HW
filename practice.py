string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
new_string = string.replace(",", "")

print(new_string)
print(string.rfind("s"))
print(string.count("i") + string.count("I"))
print(new_string[new_string.find("si"):new_string.find(" of")])
print(3 * new_string[:len(new_string)//2-1] + new_string[len(new_string)//2-1:])