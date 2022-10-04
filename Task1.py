"""
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""

new_list = list()

for N in range(5):
    N = int(input("Enter number: "))
    new_list.append(N)

print(new_list)
