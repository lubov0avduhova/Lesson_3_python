#    Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#     Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def find_middle():
    if len(list_numbers) % 2 != 0:
        return int((len(list_numbers) / 2) + 1)
    else:
        return int(len(list_numbers) / 2)


def find_multiply(list_num, length):
    first_num = 0
    last_num = -1
    i = 1
    list_result = []
    
    for items in list_num:
        list_result.append(list_num[first_num] * list_num[last_num])
        first_num += 1
        last_num -= 1
        
        if (length == i):
            return list_result
        i += 1

list_numbers = [2, 3, 4, 5, 6]

middle_length = find_middle()

print(find_multiply(list_numbers, middle_length))
