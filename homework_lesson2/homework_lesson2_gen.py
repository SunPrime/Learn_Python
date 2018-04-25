def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

def main():
    len_range = int(input("Введите число: "))
    a = my_range(len_range)
    for i in a:
        print(i)

main()