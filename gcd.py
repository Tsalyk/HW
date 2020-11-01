a = int(input("Enter: "))
b = int(input("Enter: "))

try:
    if a > b:
        if a % b == 0:
            print(b)
        else:
            while a % b != 0 and b % a != 0:
                while a > b:
                    if a % b != 0:
                        a %= b
                    else:
                        print(b)
                        break
                while b > a:
                    if b % a != 0:
                        b %= a
                    else:
                        print(a)
                        break
            if a > b:
                print(b)
            else:
                print(a)
    else:
        if b % a == 0:
            print(a)
        else:
            while a % b != 0 and b % a != 0:
                while a < b:
                    if b % a != 0:
                        b %= a
                    else:
                        print(a)
                        break
                while a > b:
                    if a % b != 0:
                        a %= b
                    else:
                        print(b)
                        break
            if a > b:
                print(b)
            else:
                print(a)
except ZeroDivisionError as err:
    print(err)
