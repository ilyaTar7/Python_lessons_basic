# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print("Задание 1")
list = [1,2,4,0,6]
list_sqr = [s**2 for s in list]
print("Список квадратов элементов: ", list_sqr)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("Задание 2")
listFirst = ["банан","персик","яблоко","киви","манго","мандарин","апельсин"]
listSecond = ["маракуйя","хурма","яблоко","лимон","манго","личи","апельсин","папайя","киви"]
listResult = [el for el in listFirst if el in listSecond]
print("Эти фрукты оказались неуникальными: ", listResult)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("Задание 3")
import random
listRandom = [random.randint(-10,10) for _ in range(20)]
print("Случайный список сформирован: ", listRandom)
listTotal = [x for x in listRandom if x%3==0 and x>0 and x%4!=0]
	# listTotal = [x for x in listRandom if x%3==0 if x>0 if x%4!=0] 
	# это тоже работает. Верна ли такая запись?
print ("Список отсортирован: ", listTotal)

