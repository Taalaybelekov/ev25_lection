# Типы данных
# int -целочиленные
# float - 2,553  :
# number = 5 # (переменная)
# print(number)
# number = 12
# print(number)
# a = 5
# b =15
# result =a+b
# print(result)
# abc - нижний регистр
# ABC - верхний регистр
# a = 100
# b = 1000
# c = 500
# d = 56.20
# print(a+b+c+d)
#
# nam1 = 996
# nam2 = 67.55
# print(nam1-nam2)
# *
# num1 = 55
# num2 = 199988
# print('результат', num1*num2)
# num1 = input('Vedite chislo')
# print(type(num1))
# num = input('vedite chislo') #-Любой цифра текст когда запрашиваешь он сохранает в строку
# print(type(num))
# num = int(input('vedite chislo'))
# print(type(num))
# num1 = int(input('Vedite chislo'))
# num2 = int(input('Vedite chislo'))
# result = num1*num2
# print(result)
# / обычное деление
# // целочисленное деление (деление без остатка)
# % - Модульное деление (возваращяет остаток от деления)
# num1 = 25
# num2 = 12
# print(num1 / num2)
# print( num1 // num2)
# print(num1 % num2)
# ** -возвидение степень
# num1 = 5
# print(num1 ** 100)
# pow(a,b)- функция возвидение степень а возводит на b
# print(pow(5, 3))
# print(pow(5, 3, 13)) #5**3/13
# divmod(a, b) оно выводит 2 чила
# первое это результат целочисленного деления (//),
# а второе это модульное деление (%)
# res = divmod( 32, 2)
# print(res)
# round()- округление
# res = 24 / 13
# print(round(res))
# print(round(res, 3))
# abs()- абсолютное значение  abs(-5) = 5 всегда возврашает положительное число
# print(abs(-100))
# print(abs(50))
# importS = π × r2 math
# print(math.pi)
# print(math.sqrt(16)) # корень
# print(math.sqrt(101))
# from math import pi ,sqrt #- можно импортировать отдельные модули
# print(pi)
# print(sqrt(100))
# dir () - Возврашяет методы обекта или функции определенного модуля
#import math
#print(dir(math))

#Множественное присваевание
#a = 5
#a, b, c = 1, 3 ,4
#v =5
#n = 7 
#d = 3
#v, n, d = d,v,n
#print(v,n,d)
##############################
#print('hello' *3 )
# str1 ='12'
# num1 = 2
# print(str1 + str(num1))
# Инкримент и Дикремент
# Инкримент -- увеличение значения какой либо переменной (a = 1 ) (a += 1) это тоже самое a=a+1;
# a = 0
# a +=1
# print(a)
#Дикримент-- уменщение значения какой либо переменной
# a = 0
# a -= 1
# print(a)
# a = 1
# a *=2
# print(a)
#  И делит можно также  также можно % //
# id -- возврещает номер ячейки памяти
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# практика
# a = float(input('ведите число'))
# b = float(input('ведите чилоо'))
# resl = a**b
# print(resl)
#  Модуль  random - предоставляет нам функции для генерации случайных чисел или буквы символы
# import  random
# print(dir(random))
# import random
#
# num = random.randint(1111, 9999)
# print(num)
# from random import choice
# import string
# print(string.ascii_letters) - выводит все буквы
# a = choice(string.ascii_letters)
# print(a)
# from math import pi
#
# r = float(input(' ведите радиюс окружности'))
# S = pi*(r**2)
# P = pi*r*2
# print('Площадь круга ', round(S))
# print('Периметр', round(P))

