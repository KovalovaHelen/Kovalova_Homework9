"""
Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

A = list()
N = int(input("Enter number N: "))

for i in range(N):
    N = int(input("Enter number: "))
    A.append(N)
print(A)
print(A[::-1])
