#   Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
#   значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните,
#   что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.


array_1 = [0, 4, 6, 1, 10, 12, 45, 15, 61, 12]
array_2 = []

for i in range(len(array_1)):

    if array_1[i] % 2 == 0:
        array_2.append(i)

print(array_1)
print(array_2)