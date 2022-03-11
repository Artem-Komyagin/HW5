# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
en=''
with open('numbers.txt', 'r') as file_obj:
    en =file_obj.read()
ru=en
for el_en,el_ru  in dictionary.items():
    ru=ru.replace(el_en,el_ru)
print(ru)
with open('numbers_ru.txt', 'w') as file_obj_ru:
    file_obj_ru.write(ru)

