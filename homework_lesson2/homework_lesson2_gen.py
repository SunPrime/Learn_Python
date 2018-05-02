#функция rangeс помощью yield
def my_range(a, b, c):
    while a < b:
        yield a
        a += c

def main():
    len_range_start = int(input("Введите начало: "))
    len_range_finish = int(input("Введите конец: "))
    len_range_step = int(input("Введите шаг: "))
    for len_range_start in my_range(len_range_start, len_range_finish, len_range_step):
        print(len_range_start)

main()