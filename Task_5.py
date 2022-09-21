

#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#     Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def find_fibonachy(number):
    list_num_left_part = [0,1]
    list_num_right_part = [0,1]
    i=2
    while i <= number:
        list_num_right_part.append((list_num_right_part[i-1])+list_num_right_part[i-2])
        list_num_left_part.append((list_num_left_part[i-1] *(-1))+list_num_left_part[i-2])
        i+=1
    list_num_left_part.reverse()


    print(list_num_left_part+list_num_right_part)
        
number = int(input('Введите число: '))
find_fibonachy(number)