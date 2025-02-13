import time


def print_time(func):
    def wrapper(arg1, arg2, arg3):
        result = func(arg1, arg2, arg3)
        print("系统现在时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return result

    return wrapper


@print_time
def add_to_set(a, b, c):
    my_set = set()
    my_set.add(a)
    my_set.add(b)
    my_set.add(c)
    print("Set:", my_set)


add_to_set(1, 2, 3)
