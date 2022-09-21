

#     Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19


def remove_before_dot():
    new_list = []
    for i in list_numbers:
        float_number = i
        int_number = int(i)
        new_list.append('{:.2f}'.format(float_number - int_number))
    return new_list

def find_max_and_min(new_list):
    min_num = float(0)
    max_num = new_list[0]
    i = 1
    for i in new_list:
        if(i > max_num):
            temp = max_num
            max_num = i
            i = temp
        else: min_num = i
    return max_num, min_num

def find_result(max_num, min_num):
    return float(max_num) - float(min_num)
    


list_numbers = [1.1, 1.2, 3.1, 10.01]
result = remove_before_dot()
max_num, min_num = find_max_and_min(result)

print(find_result(max_num, min_num))