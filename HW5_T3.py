# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#
#
sum_salaries=0
list=[]
with open('names.txt', 'r') as file_obj:
    content=file_obj.readlines()
    # print(content)
    for line in content:
        el=line.split()
        list.append([el[0], float(el[1])])
        print(f"{el[0]}: {float(el[1])} руб.")
        sum_salaries += float(el[1])
    print(' ')
    print(f'average salary is {sum_salaries.__round__()/len(list)}')

print('emploers with salary less 20000 : ')
[print(elem[0]) for elem in list if elem[1]<20000]

print("\nСотрудники с окладом менее 20000 руб.")
[print(worker[0]) for worker in report if worker[1] < 2000]
# print(list2)
