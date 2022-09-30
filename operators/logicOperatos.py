# Операторы сравнения
# Условные операторы
# Логические операторы

# Оператор сравнение
# <,>,  ==,  <=, >=, !=(не равно)
# 1<5 -> True
# 7>9 -> False
# num1 = 15
# num2 = 16
# print(num1 == num2)
# num2 = 15
# print( num1 == num2)
#####################################
# stroka1 = 'Hello'
# stroka2 = 'Word'
# print(stroka1 > stroka2)
# строки сравнивает по оски коды (смотреть по фото) в длинных строках сравнивает только первый синвол

#как выташить аски код
# print(ord('H'))
# print(ord('в')) возврашает аски код
#print(chr(1074), chr(74)) #возврашает синвол

# stroka1 = 'Hello!'
# stroka2 = 'World'
# print(len(stroka1) > len(stroka2))
# stroka2 = 'World   '
# print(len(stroka1) > len(stroka2))

#Условные операторы
# if
# elif
# else:
# if <условия>:
#     <bodi if>  сработает если в выражение иф придет Thre
# elif <condition>:
#     <body elif>
# else:
#     <body else> срабатывает если во всех выше стояших условиях пришло False

# string = input('Enter smt')
# if string.lower() == 'hello':
#     print('Hello kak dela')
# elif string.lower() == 'john':
#     print('Welcome back John Snow ! The king of North')
# elif string.lower() == 'abra':
#     print('Sim Salomon')
# else:
#     print('sovpodeni NET')

# email = input('enter email')
# password1 = input('enter the password:')
# if len(password1) < 8:
#     raise ValueError('pasword too short') #raise это чтобы остановить код
# password2 = input('enter the password confirmation:')
# if password2 != password1:
#     raise ValueError(' Pasword didn\'t match')
# else:
#     print('Uspeshno zaregalsa')

# age =input('enter your age')
# if age.isdigit():
#     age = int(age)
# else:
#     print('invalid (oshibaka)')
#     raise Exception('stop')
# if age < 18:
#     print(f'ne prodadim Prihodi cherez {18 - age} let')
# else:
#     print('Mojno kupit')

#Логические операторы
# and - логическое и
# or - логическое или
# not - логическое отрецание

# my_age = 20
# your_age = 18
# result =my_age ==20 and your_age ==18 #должно совподать оба условия
# print(result)
#
# result = my_age ==20 or your_age == 19 # здесь должно хотябы одно дожно совподать
# print(result)
#
# result = not my_age == 20 # если не
# print(result)
#####################################################################
# user = 'John'
# is_google_user = False
# is_githab_user =True
# is_age_greater_21 = True
# user_coins = 4000
# # либо юзера или гитхаба  и либо возраст 21 либо бабки (8000)
# if is_google_user or is_githab_user and is_age_greater_21 or user_coins:
#     print(f'Vy mojete zaxodit Mr/Mrs {user}')
# else:
#     print('sory')
#########################################################################
# Операторы индикации
# in -проверяет наличие элемента внутри кого либо интерируемого объекта (строки, списки и т д)
# is - сравнивает ячейки памяти длух объектов (==)
# is not - отрицательное сравнение ячеек памяти

# str1 = 'Hello word'
# print(str1)
# choice = input('Enter the symbol:')
# if choice in str1:
#     print(f'The symbol: {choice} exist')
# else:
#     print(f'The symbol: {choice}  does not exist')

###########################################################################################

