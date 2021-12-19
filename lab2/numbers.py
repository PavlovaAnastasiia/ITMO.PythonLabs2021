
a = input("Введите число: ")
b = input("Введите еще одно число: ")

c = int(a) + int(b)
print(c)

a1 = int(15)
b1 = int(3)
c = a1/b1
print(c)

#не выполняется
#param = "string" + 15
#print("param", param)

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

#форматирование строк
a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:7.3f}".format(n3))