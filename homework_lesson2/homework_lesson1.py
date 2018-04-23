#form a list of random numbers
def random_list(len_list):
    from random import randint
    list_mumerals = []
    for i in range(len_list):
        a = randint(0, 100)
        list_mumerals.append(a)
    return list_mumerals

# minimum numbers
def min_number(input_list4min_numbers):
    result = 101
    for i in range(len(input_list4min_numbers)):
        num = input_list4min_numbers[i]
        if result > num:
            result = num
    return result

#maximum number
def max_number(input_list4max_number):
    result = 0
    for i in range(len(input_list4max_number)):
        num = input_list4max_number[i]
        if result < num:
            result = num
    return result

#сортировка строки "пузырьковым методом" без рекурсии
def sort_ar(ar1):
    c = 0
    for i in range(len(ar1)):
        j = i + 1
        for j in range(i, len(ar1)):
            if ar1[i] > ar1[j]:
                c = ar1[i]
                ar1[i] = ar1[j]
                ar1[j] = c
    return ar1

#сортировка вставками без рекурсии
def insertion_sort(x):
    for i in range(len(x)):
        num = x[i]
        j = i
        while (j > 0 and x[j - 1] > num):
            x[j] = x[j - 1]
            j -= 1
        x[j] = num
    return x

abc = int(input("Введите длину строки: "))
list1 = random_list(abc)
print(list1)
print("Минимальное число = ", min_number(list1))
print("Максимальное число = ", max_number(list1))
print("Сортировка пузырьком (без рекурсии): ", sort_ar(list1))
print("Сортировка вставками (без рекурсии): ", insertion_sort(list1))