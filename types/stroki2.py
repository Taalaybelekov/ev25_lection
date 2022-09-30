#print(dir(str)) # методы строк
#replace(old,new,[count]) - меням в стороке олд на new значение, если вы укажите count
#то он заменит ровно коунт раз...
# text = 'ha ha ha ha '
# result = text.replace('a', 'i',2)
# print(text)
# print(f'result after replace: {result}')
###################################################
# str1 = 'Hello word ! My name is John Snow'
# res = str1.replace('John', 'Jamie')
# res = res.replace('Snow','Lanister')
# print(res)
########################################
# print(id('H'))
#print(id('h')) # две разные айдишники разные верхний и нижный регистр
 #######################
 #strip()  -- убирает пробелы символы в начале и в конце строки
# rstrip, lstrip
# text = input('enter text')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)
# print(len(res))
##3############################################
# text = '     Hello Word!    '
# print(len(text))
# res =text.rstrip()
# print(res)
# print(len(res)) # Также lstrip убирает пробелы с лева
#######################################
# isdigit -
# isnumeric
# isdecimal
# Это три метода состоит ли наша строка из чисел
# text = '57'
# print(text.isdigit())
# text = '5755h'
# print(text.isdigit())
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops tam est ne chislovoi sinvol')
#######################################################
# isalnum -- проверяет состоит ли наша строка из чисел и символов
# латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())
##################################################

#isalpha --- проверяет состоит ли строка польностю из алфавита (латиница кирилица)
# text = 'Hello world'
# print(text.isalpha())
# print(text[:5].isalpha())
# text = 'Helloword'
#
# print(text.isalpha())
# islower
# isupper
# istitle -- каждое слова если начинается верхнем регистре (Привет Как Дела ) True
# возврашает верхний и нижний и первых верний то True

#index(value,[start],[end]) выводит индекс значения value которое мы передаем в нашей строке
# text = 'Hello world ! My name is John Snow'
# print(text.index('John'))
# print(text[25])
# print(text.index('o',5)) # здесь он нашел после 5 индекса  (world)
##############################################
#count (value,[stat]) считает количество вхождений value в нашу строку
# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))
######################################################
# text = input('Enter text')
# i = 0
# while i<=text.count('o'):
#     print(i)
#     i+=1 # инкримет
#####################
# text = input('Enter text')
# i = 0
# res = -1
# while i<text.count('o'):
#     res =text.index('o',res+1)
#     print(res)
#     i+=1 # инкримет
#####################
# find(value,[start],[end]) -- делает тоже самое что и index но есть одно отличие, в том что если
# value нет в строке то возврашает -1
# text = 'Hello'
# print(text.find('l'))
# print(text.index(hi))

# swapcase -переводит все регистры в противоположный регистр
# upper() все в верхний регистр
# lowear() все в нижний регистр
# text = 'Helo WORD'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())
#capitalize() -- переводит первую букву в верхний регистр
# name = input('enter name').capitalize()
# print(name)
#################################
#title -- переводит первые буквы всех слов в верхний регистр
# text =input('vedite text ').title()
# print(text)

# split(разделитель)-- он дробит строку по разделителю который находится в строке
# все части строки сохраняются в тип данных list
# text = 'let me speak from my hearth in English! Cause My name is John Snow!'
# ls =text.split(' ')
# print(ls)
# print(len(ls))
# ls = text.split('o')
# print(ls)
##############################################
#'разделитель'.join(__iterable=(list)) --- соединяет по разделителю сторки которые находится в list
# text = 'let me speak from my hearth in English! Cause My name is John Snow!'
# ls =text.split(' ')
# print(ls)
# print(len(ls))
# res =' '.join(ls)
# print(res)
# res = '@'.join(ls)
# print(res)

