# string - Строки
#  'Hello word' "hello word"
#  """
#  hello word
#  my name is John
#  """
# # Строки -- это набор последовательных символов которые
# мы используем для хранения и предостовления текстововой информации.
# набор методов и операции которые мы можем использовать с данными
# в виде текста
# индиксация строки
# name = 'John'
# #  j = 0 = -4
# #  o = 1 = -3
# #  h = 2 = -2
# #  n = 3 = -1
# print(name[-1])
# print(name[1])
# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[-3], str1[-2], str1[-1])
#  это 2 вида индексации (вывод индексации)
# Срезы по индексам ------
# [start: end: <step>]
# str1 = 'birthday'
# str2 = str1[0:5]
# print(str2)
# print(str1[5:15])
# print(len(str1)) # len - узнать длину строки
# print(str1[:7])
text = 'Hello world! my name is John \' I m North King'
# print(len(text))
# print(text[:12])
# print(text[13:29])
# print(text[30:])
# print(text[:12:2])
# print(text[::2])
# print(text[::-1]) #это переводит с конца
# print(text[:12:-1])
# Конкантенация строк (слияния, соединение)
# worl1 = 'Hello'
# worl2 = 'World'
# probel = ' '
# result = worl1 + probel + worl2
# print(result)
# print(worl1 + ' ' + worl2) -Или так можно
# ФОРМАТИРОВАНИЕ СТРОК
# 3 вида есть 1) %  2) .format()
# 3)Интерпритация строки f-строки
# name =input('enter your name')
# last_name = input('Last name')
# print('hello, my name is',name ,last_name)
# print('hello, my name is'+ '' + name ,last_name)
# print('hello, my name is %s %s' %(name ,last_name)) # %s -
 # .format
# name =input('enter your name')
# last_name = input('Last name')
# print('Hello, My name is {} - {}'.format(name,last_name))
# print('Hello, My name is {} - {}'.format(last_name,name))
 # f -строки
# name =input('enter your name')
# last_name = input('Last name')
# print(f'hello, my name is { name  } -> {last_name} ')
# Экронирование строк -- механизм при помоши которого можно вставлять симвлы, которые сложно ввести с
# клаваиатуры в строку
# \n -перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция
# name = 'john\nSnow'
# lastName = '\vSnow'
# last_name ='\tSnow'
# print(name)
# print(lastName)
# print(last_name)

