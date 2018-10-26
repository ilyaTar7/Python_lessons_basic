print ('Задание-1:')
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    i = 2
    listOne = [1, 1]
    while i < m:
        a = listOne[i - 1] + listOne[i - 2]
        listOne.append(a)

        i = i + 1

    return listOne[n-1: m]


print(fibonacci(4, 9))
print(fibonacci(4, 5))

print ('Задание-2:')
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    list = []
    for i in range(len(origin_list)):
        list.append(min(origin_list))
        del origin_list[origin_list.index(min(origin_list))]
    origin_list = list
    return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


print ('Задание-3:')
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_fi(arg,list):
    list1 = []
    for i in list:
        if i != arg:
            list1.append(i)
    return list1
print(my_fi(1,[1,2,3,4,2,1,5,6,7,1,8,9,1,5]))

print ('Задание-4:')
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def parallelogram(a, b, c, d):
    result = ''

    if abs(int(a[0]) - int(b[0])) == abs(int(c[0]) - int(d[0])) and abs(int(a[1]) - int(b[1])) == abs(int(c[1]) - int(d[1])):

       result = ("Точки являются вершинами параллелограмма")
    else:
        result = ("Точки не являются вершинами параллелограмма")
    return result

print(parallelogram([1,1],[2,2],[3,3],[4,4])) # да
print(parallelogram([3,1],[3,2],[3,3],[9,4])) # нет