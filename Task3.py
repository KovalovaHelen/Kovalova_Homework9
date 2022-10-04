"""
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""

A = list()

for x in range(10):
    x = int(input("Enter number: "))
    A.append(x)

print(A)

N = int(input("Enter number N: "))
print(A.count(N))
