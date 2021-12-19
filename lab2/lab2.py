
string1 = "This is string."
string2 = " This is another string."
string3 = string1 + string2
print(string3)

print(len(string1)) #определяет длину строки
print(string2.title()) #преобразует первый символ каждого слова в строке к верхнему регистру
print(string2.lower()) #символы строки преобразуются к нижнем регистру
print(string3.upper()) #символы строки преобразуются к верхнему регистру;
print(string1.rstrip()) #удаляются пробелы в конце строки;
print(string2.lstrip()) #удаляются пробелы в начале строки;
print(string3.strip()) #удаляются пробелы с обоих концов;
print(string3.strip('0')) #удаляются с обоих концов указанные символы в параметре функции.

d = "qwerty"
ch = d[2] #извлекается символ "e"
print(ch)

chm = d[1:3] #срез строки
print(chm)
chm1 = d[1:]
print(chm1)
chm2 = d[:3]
print(chm2)
chm3 = d[:]
print(chm3)
chm4 = d[1:5:2]
print(chm4)
