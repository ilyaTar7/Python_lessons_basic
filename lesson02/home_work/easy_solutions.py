print("Задача-1")
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
fruits = ("яблоко", "банан", "киви", "манго", "кокос") #задаём элементы списка
for i in range(len(fruits)):
    print('{}.'.format(i+1), '{:>6}'.format(fruits[i]) )

print("Задача-2")
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
import random

list1 = []
list2 = []
for i in range(10):
    list1.append(random.randint(10, 29))
    list2.append(random.randint(10, 29))
print('Список #1 {}''\n''Список #2 {}'.format(list1,list2))
for a in list2:
        if a in list1:
            list1.remove(a)
print ('Результат после сравнения:',list1)


print("Задача-3")
# Дан произвольный список из целых чисел.
list3 = []
for i in range(10):
    list3.append(random.randint(0, 100))
print('Список сформирован',list3)
listNew = []
for element in list3:
    if element%2 == 0:
        listNew.append(element/4)
    else:
        listNew.append(element*2)
print('Вычисления выполнены!')        
print('Получен новый список', listNew)
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен,
# то умножить на два.