my_list = [1, 2, 3]
print(my_list)
#my_list[0] = 100
print(my_list)
#Список изменился, так как списки является изменяемыми объектами.

my_tuple = (1, 2, 3)
print(my_tuple)
#my_tuple[0] = 100
#Кортеж не изменился, так как кортежи являются неизменяемыми объектами

my_string = "cat"
print(my_string)
#my_string[0] = 'b'
print(my_string)
my_string = 'b' + my_string[1:]
#Строка неизменяемая, поэтому изменить отдельный символ нельзя.