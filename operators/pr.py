# sentence = input('Введите предложение: ')

# if sentence[-1] == '?':
#     print('Предложение вопросительное')
# else:
#     print('Обычное предложение')


# sentence = input('Введите предложение: ')
# print('Предложение вопросительное' if sentence [-1] == '?' else 'Обычное предложение')




# ------------------------------------------------------------------------------------------------------------------------------------------------
# Ternary operator (Тернарный оператор) - конструкция, которая аналогична по своим свойствам
# и действию конструкции if/else, но при этом записывается в одну строчку кода
# <выражение если в условии True> if <условие> else <выражение если False> //////

# number = 18
# res ='even number' if number % 2 == 0 else 'odd number'
# print(res)
####################################################


# from string import digits
# symbol = digits + '-'
# print(symbol)
# number = input('Vedite chislo')
# is_correct = True
# for i in number:
#     if i not in symbol:
#         is_correct = False
#
# if is_correct:
#     print('Yes number !')
#     number = int(number)
#     print('your number: ', number)
#     result = number if number >=0 else -number
#     print(result)
# else:
#     print('Invalid values')
#

# CALCULAT
# from string import digits
#
# flag = True
# symbols = digits + '-' + '.'
#
# while flag:
#     is_correct_number = True
#     num1 = input(' vedite pervoe chislo : ')
#
#     if len(num1) <= 1 and (num1 == '.' or num1 == '-') and num1:
#             is_correct_number = False
#     for x in num1:
#
#         if x not in symbols:
#             print(' Vy veli nepravelnoe chislo')
#             is_correct_number = False
#             break
#     num2 = input(' vedite pervoe chislo 2: ')
#
#     if len(num2) <= 1 and (num2 == '.' or num2 == '-') and num2:
#             is_correct_number = False
#     for x in num2:
#
#         if x not in symbols:
#             print(' Vy veli nepravelnoe chislo')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#             continue
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     # print(num1)
#     # print(num2)
#     what = input('что делаем (+.-.*./.%.**.//): ')
#
#     if what == '+':
#         res = num1 + num2
#         print('Результат: '+str(res))
#     elif what == '-':
#         res = num1 - num2
#         print('Результат: '+str(res))
#     elif what == '*':
#         res = num1 * num2
#         print('Результат: '+str(res))
#     elif what == '/':
#         if num2 == 0:
#             print('на ноль нельзя делить')
#         else:
#             print(f'Результат: {num1 / num2}')
#     elif what == '%':
#         res = num1 % num2
#         print('Результат: '+str(res))
#     elif what == '**':
#         res = num1 ** num2
#         print('Результат: '+str(res))
#     elif what == '//':
#         res = num1 // num2
#         print('Результат: '+str(res))
#     else:
#         print('Вы ввели неправельную операцию')
#
#     choice = input('Hotite ostanovit (yes)' )
#     if choice.lower() == 'yes':
#         flag = False
#         print('Poka')


#####################################################
# a = {'x': 1, 'y': 2, 'z': 1}
# for key in a:
#     print(key)
#     break

# a = {'a': 1, 'b': 2, 'c': 1}
# s = a.popitem()
# print(s)

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# s = []
# for key in a.keys():
#     s.append(key)
# print(s)

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# a = {'a': 1, 'b': 2, 'c': 1}
# for ke1y in a.keys():
#     print(key)

# a = {'a': 1, 'b': 2, 'c': 1}
# for v in a.values():
#     print(v)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = a.copy()
# for k, v in b.items():
#     if v % 2 == 0:
#         b[k] = 2
# print(b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for k,v in a.items():
#     if v != None:
#         b[k] = v
#
# print(b)

''' a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# b={}
# for k,v in a.items():
#     if v!=0
#
# print(b) ???????'''

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b={}
# for k,v in a.items():
#     if v%2!=0:
#         b[k]=v
# print(b)

# a = {'a': 1, 'b': 2, 'c': 3}
# b={}
# for k,v in a.items():
#     b[v]=k
# print(b)


# a = {'a': 3, 'b': 2}
# total=sum(a.values())
# print(total)


dict_ = {'x': 1, 'y': 2, 'z': 1}
print(dir(dict_))
