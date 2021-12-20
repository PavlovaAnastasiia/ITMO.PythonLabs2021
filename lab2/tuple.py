print((dir(tuple)))

help(tuple.index)
help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8)) #количество восьмерок
print(seq.index(44)) #индекс значения 8
listseq = list(seq) #преобразование в список
print(listseq)
print(type(listseq))

#Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D)
print(D['food'])
D['quantity'] += 10
print(D['quantity'] + 10)

dp = {}
key = input("Введите название ключа: ")
val = input("Введите значение: ")
dp[key] = val
print(dp)

#Вложеность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'], 'age': 25}
print(rec["name"]["firstname"], rec["name"]["lastname"])
print(rec["name"]["firstname"])
print(rec["job"])

rec['job'].append('janitor')
print(rec)