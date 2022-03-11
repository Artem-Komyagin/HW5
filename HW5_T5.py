# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('t5.txt', 'w') as file_obj:
    num = input('write num- ')
    file_obj.write(num)
list_int=[]
with open('t5.txt', 'r') as file_obj1:
    list_str=file_obj1.readline()
    list=list_str.split()
    list_int=[int(el) for el in list]
    print(sum(list_int))