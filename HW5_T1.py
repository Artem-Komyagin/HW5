# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('test1.txt', 'w') as file_obj:
    new=input('write smth -')
    file_obj.write(new+'\n')
while new!='':
    new = input('write smth -')
    with open('test1.txt', 'a') as file_obj:
        file_obj.write(new+'\n')
with open('test1.txt', 'r') as file_obj2:
    content = file_obj2.read()
    print(f'the content is down\n {content}')