"""
Задание 7:
Пользователь вводит текст нужно вывести количество цифр в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество цифр: 3
"""

digits = 0
text = input("Введите текст: ")
print(text)

for i in text.split():
    if i.isdigit():
        digits += 1

print(f"Количество цифр: {digits}")
