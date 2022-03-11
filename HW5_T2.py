# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('test1.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print (f'there are {len(content)} lines in the file')
    for l,w in enumerate(content):
        words=w.split()
        print(f'in {l+1} - {len(words)} words')