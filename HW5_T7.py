# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
list=[]
with open('t7.txt', 'r') as file:
    text=file
    profits={}
    profit_sum=0
    for el in file:
        items=el.split()
        profit=int (items[2]) - int(items[3])
        if profit>0:
            profits.update({items[0]: profit})
            profit_sum +=profit
    list.append(profits)
    list.append({'average profit': (profit_sum)/ len (profits)})

with open('t7.json', 'w') as json_file:
    json.dump(list, json_file)
json_list= json.dumps(list)

print(text)
print(list)
print(json_list)


