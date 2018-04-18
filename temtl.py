slovar = [[1,2],
         [3,4],
         [5,6]]
#print(slovar[1][0])

ar1 = [[80, 12, 4, 27, 8, 15],
       [20, 13, 1, 2, 16, 15],
       [60, 45, 67, 23, 1, 54],
       [70, 68, 14, 12, 4, 6],
       [10, 5, 6, 90, 78, 67],
       [25, 13, 20, 58, 4, 19]
       ]

ar2 = [[5, 6, 1, 11],
       [10, 8, 13],
       [2, 5, 3],
       [2,5,8]
       ]

#сортировка без рекурсии
def bubble_sort(input_array):
    c = 0
    for i in range(0, len(input_array)):
        for j in range(0, len(input_array[i])):
            k = j + 1
            for k in range(0, len(input_array[i])):
                if input_array[i][j] < input_array[i][k]:
                    c = input_array[i][j]
                    input_array[i][j] = input_array[i][k]
                    input_array[i][k] = c
    for row in input_array:
            for elem in row:
                print(elem, end=' ')
            print()

bubble_sort(ar2)
bubble_sort(ar1)