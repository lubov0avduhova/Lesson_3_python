
#     Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

#     Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def find_sum():
    i = 0
    sum_numbers = 0
    for items in list_numbers:
        if (i % 2 != 0):
            sum_numbers += items
        i += 1
    print (sum_numbers)


list_numbers = [2, 3, 5, 9, 3]
find_sum()