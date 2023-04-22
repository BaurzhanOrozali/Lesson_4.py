def zadanie1():
    num = int(input('Введите ваше число: '))
    lis = []
    count = 2
    flag = True
    while  num > 1:
        if num % count == 0:
            num = num/count
            lis.append(count)
        elif num % count !=0:
            count +=1
    print (lis) 
      


def zadanie2():  
    fruits_assortiment = {'абрикос', 'бананы', 'виноград', 'груша', 'яблоко'}
    fruits_sklad = {'абрикос', 'виноград', 'груша', 'яблоко'}
    print ('на складе закончились:', *fruits_assortiment.difference(fruits_sklad))
from math import pi



#пример 0,0001 ->3,1415    0,01 -> 3,14
def tyr ():
    num = str(input('введите ваше число: '))
    return ''.join(reversed(num))
def zadanie3():
    ty = str(tyr ())
    x = ','
    count = 0
    flag = True
    while flag:
        for i in range(len(ty)):
            if ty[i] != x:
                count+=1
            flag = False
    print(count-1, ' числа оставить после запятой.')
    print('результат: ', round(pi, count-1))
