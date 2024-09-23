immutable_var = ([1,2],1,2,'a','b')
print('Immutable tuple: ',immutable_var)
print('пробуем изменить элемент кортежа №4:  ',immutable_var[4])
print("TypeError: 'tuple' object does not support item assignment")
# Попытка изменить элемент кортежа №4:
#immutable_var[4] = 'c'
# Получаем:
#
# Traceback (most recent call last):
#   File "C:/Users/Nick/PycharmProjects/pythonProject5/module_1_5.py", line 4, in <module>
#     immutable_var[4] = 'c'
# TypeError: 'tuple' object does not support item assignment
#
# Выдаёт ошибку, т.к. переменная immutable_var, является кортежем и относится к классу неизменяемых объектов
#
# Однако:
print()
immutable_var[0][1] = 5
print('Immutable tuple: ',immutable_var)
print('В элементе кортежа с индексом "0", заменил эелемент списка № "1"')
print()
#
# Это возможно, т.к. элемент кортежа с индексом "0" в свою очередь является спмском.
# Меняетя не элемет кортежа, а объект списка с индексом "1"
mutable_list = [[3,4],3,4,'c','d']
print('Mutable list:  ',mutable_list)
#
mutable_list.pop(0) # Удаление элемента списка по индексу
print('Mutable list Modified: ',mutable_list)
