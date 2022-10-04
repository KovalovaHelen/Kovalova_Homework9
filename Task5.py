"""
Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

A = list()
C = list()

for i in range(5):
    i = int(input("Enter number: "))
    A.append(i)
print(A)

for i in A:
    if i > 5:
        C.append(i)
print(C)
