

#     Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#     Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# n = int(input())
 
# b = ''
 
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2

def find_binary_number(number):
    result = []
    while (number > 0):
        result.append(number % 2)
        number = int(number / 2)
    result.reverse()
    return print(result)

number = int(input('Введите число: '))
find_binary_number(number)

# print(bin(number))
