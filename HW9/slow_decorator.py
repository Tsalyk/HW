"""
    Напишите декоратор, который будет замедлять выполнение функции на 5 секунд.
    Если функция выполняется более 10 секунд (с учетом замедления), то
    дополнительно выводить сообщение f'{func.__name__} - very slow function'
"""
import time

def decorate(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(5)
        func()
        end = time.time() - start

        if end > 10:
            print(f"{func.__name__} - very slow function")
    return wrapper

@decorate
def some_func():
    return 10**10000000

some_func()