def sum(a, b):
    return a + b

#функция высшего порядка
def high_func(a, b, c, func):
    return c + func(a, b)

#компаратор
def comparator(a,b):
    if a > b: return 1
    if a < b: return -1
    return 0

#сортировка массива
def sort(massive, comparator):
    for i in range(len(massive)):
        for j in range(i + 1, len(massive)):
            if comparator(massive[i], massive[j]) == 1:
                massive[i], massive[j] = massive[j], massive[i]

print(high_func(10,20,30,sum))

massive = [10,30,5,40,23,60]

sort(massive,comparator)

print(massive)