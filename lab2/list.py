
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))

help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

print(list1)
list1[3] = 234
list1[0] = 0
list1[2] = 33
print(list1)
list1.insert(10, 13)
print(list1)
list1.remove(8) #по значению
print(list1)
list1.append(22) #добавление элемента в конец списка
print(list1)
item = list1.pop() #удаляет последний элемент
print(list1, item)
del list1[4]  #удаление по позиции
print(list1)

#сортировка элементов списка
list1.sort(reverse = True)
print(list1)
list = sorted(list1)
print(list)

list2 = [3, 5, 6, 2, 33, 6, 11]
print(list2)
lis = sorted(list2)
print(lis)