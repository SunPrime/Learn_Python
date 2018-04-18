"""def my_func(*args): #для списка, для словаря **kwargs
    return args[0]

d = my_func(1,20) # функция вернет только первый єлемент списка
print(d)

def my_func1(a,b,c):
    return a + b + c

print(my_func1(b = 10, c = 20, a = 30)) #переопределены значения

def main():
    a = int() # это значит что а=0 или None
    b = 1.2
    c = "Hello, word"
    d = bool() # для типа bool()=False, если 1 то True
    e = list() #пустой список
    spisok = [1,2,3,4,5]
    slovar = [[1,2],
              [3,4],
              [5,6]]
    print(slovar[2][0])
    temp = [7,8]
    slovar.append(temp)
    print(slovar)
    spisok.append(10)
    print(spisok)
    print(c, a + b)
    d1 = {"sss":10,"fff":20} #ключи должны быть уникальными
    d1["ggg"] = 90
    print(d1)
    t = tuple() #неизменяемый кортеж
    t = (10,20,30,40) #неизменяемый кортеж
    print(t[3])
    #множества, почитать про класс set
    l = [10,10,20,30,40,50,90,30]
    for element in l:
        print(element)
    s = set(l)
    copy_list = list(l)
    s = set(l)  #попробовать отсортировать после преобразования типов
    print(s)
    l1 = [i for i in range(0,101)] # генерация списков
    print(l1)

main()

#рекурсия
#считаем факториал
def fact(n):
    if n > 0:
        return (n-1) * n #фукция обращается сама к себе, пока не дойдум до значения, которое функция знает, фактически это return fact(n-1)*n
    else:
        return 1

print(fact(5))

#пример ленивого вычисления
def func(x,y):
    if x == 3:
        return x
    else:
        return y

d = func(3,g(10)) #пайтон выдаст ошибку
print(d)"""

# ханойская башня
def hanoy(n, a, b, c):
    if n > 0:
        hanoy(n-1, a, c, b)
        print("take disk " + str(n) + " from " + str(a) + " to " + str(c))
        hanoy(n-1, b, a, c)

hanoy(3, "A", "B", "C")