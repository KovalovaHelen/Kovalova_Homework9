"""
Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла
(запрещено использовать функцию min и max). Вывести эти числа.
"""

A = list()
N = int(input("Enter number N: "))

for i in range(N):
    i = int(input("Enter number: "))
    A.append(i)
print(A)

maximum = A[0]
for i in range(N):
    if A[i] > maximum:
        maximum = A[i]

minimum = A[0]
for i in range(N):
    if A[i] < minimum:
        minimum = A[i]

print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")
