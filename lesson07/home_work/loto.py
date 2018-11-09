#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import os
import sys
import random

class Kartocka:
    def __init__(self):
        #Генератор новой карточки
        possiblenumbers = [i for i in range(1,91)]

        numderkarts = []
        for _ in range(0,15):
            index = random.randint(0,len(possiblenumbers)-1) #случайный индекс из возможных
            number = possiblenumbers[index] #получили число
            possiblenumbers.remove(number) #убрали из списка возможных значение
            numderkarts.append(number)

        #Теперь у нас список всех номеров в карточке. Создадим саму карточку
        items = numderkarts.copy()

        kr = []
        for y in range(0,3):
            lines = [0 for _ in range(0,9)] #Пустая строка

            lineitems = []
            for x in range(0,5):
                index = random.randint(0,len(items)-1)
                item = items[index]
                items.remove(item)
                lineitems.append(item)
            lineitems.sort()

            index = 0
            maxfree = 0
            for x in range(0, 9):
                rnd = random.randint(0,2)
                if ((rnd == 0) and (maxfree<=4)) or (index >=5):
                    maxfree += 1
                else:
                    index += 1
                    lines[x] = lineitems[index-1]
            kr.append(lines) #Все эти пляски только чтобы по порядку были цифры

        self.__numderkarts = numderkarts
        self.__kr = kr

    def delitem(self, number):
        #удаление поля в карточке
        if number in self.__numderkarts:
            self.__numderkarts.remove(number)
            for j in range(0,3):
                if number in self.__kr[j]:
                    index = self.__kr[j].index(number)
                    self.__kr[j][index] = -1
        return len(self.__numderkarts) == 0

    def hasitem(self, number):
        #проверка есть ли номер в карточке
        result = False
        innernumder = int(number)
        if innernumder in self.__numderkarts:
            result = True
        return result

    def __sub__(self, other):
        result = self.delitem(other)
        return result

    def __mul__(self, other):
        result = self.hasitem(other)
        return result

    def __str__(self):
        #Выведем карточку. Покрасивее отформатируем
        result = ""
        for j in range(0,3):
            for i in range(0,8):
                if self.__kr[j][i] == 0:
                    result += "  "
                elif self.__kr[j][i] == -1:
                    result += "--"
                elif self.__kr[j][i] <10:
                    result += " "+str(self.__kr[j][i])
                else:
                    result += str(self.__kr[j][i])
                result += " "
            result += "\n"
        return result.rstrip()



class Loto:
    def __init__(self):
        self.sumka = [i for i in range(1,91)]

    @property
    def next(self):
        #не придумал каким генератором правильно вытащить бочонок поэтому получилось так
        index = random.randint(0,len(self.sumka)-1)
        result = self.sumka[index]
        self.sumka.remove(result)
        return result

    @property
    def count(self):
        result = len(self.sumka)
        return result

mykart = Kartocka()
compkart = Kartocka()

myloto = Loto()

exitcode = -1
exitmsg = ["Игра окончена Вы выиграли", "Игра окончена Компьютер выиграл", "Игра окончена никто не выиграл", "Ничья"]
endtrue = True
while endtrue: #гребаное предусловие, нодо еще if поставить иначе после выигрыша она еще делает один ход
    if endtrue:
        if sys.stdin.isatty(): #Если это терминал, а не IDLE то будем очищать его для красоты иначе будут ошибки
            os.system('cls' if os.name == 'nt' else 'clear')  #очистка будет работать только в терминале

        bochonok = myloto.next
        print("Новый бочонок: {} (осталось {})".format(bochonok, myloto.count))
        print("------ Ваша карточка -----")

        print(mykart)
        print("--------------------------")
        print("-- Карточка компьютера ---")
        print(compkart)
        print("--------------------------")

        #print(str(mykart * bochonok)) # проверяет есть ли в карточке бочонок
        #print(str(compkart * bochonok)) # проверяет есть ли в карточке бочонок

        answer = ""
        while not (answer.lower() == "y") and not (answer.lower() == "n"):
            #answer = input("Зачеркнуть цифру? (y/n) :")
            answer = "n"  #НЕМНОГО АВТОМАТИЗИРУЕМ
            if mykart * bochonok:
                answer = "y"

        if ((answer.lower() == "n") and (mykart * bochonok)) or ((answer.lower() == "y") and not (mykart * bochonok)):
            exitcode = 1
        if myloto.count == 0:
            exitcode = 2

        resmy = mykart - bochonok
        rescomp = compkart - bochonok
        if resmy and rescomp:
            exitcode = 3 #Ничья
        elif (resmy):
            exitcode = 0
        elif (rescomp):
            exitcode = 1

        if exitcode >= 0:
            endtrue = False

print(exitmsg[exitcode])