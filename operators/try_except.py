# Обработка исключений
# Операторы try ... except

#print('Hello world! ')
 #a=3 это синтаксическая ошибка

'''ощибки Erros -> связанные с кодом это
    SyntaxError
    IndentationError
    TabError

Исключение Exception-> ошибки связанные с неправельным данными которые 
передаются в код 
    ZeroDivisionError
    ArithmeticError
    NameError
    IndexError
    KeyError
    ValueError
    ImportError
    BaseException прорадитель всех исключений '''
# try:
#     num1 = int(input('enter the number'))
#     num2 = int(input('vedite  num2'))
#     print(num1)
# except:
#     print('ne pravel')
#
# print('очень важная строчка кода')

'''try:
    <body try>
except:
    <body excepta> сработает только если ошибка 
не обезательные 
<else:>
    <body else> сработает если в операторе try нет ошибки
<finally:>
    <body finally> работает в любом случае'''

# try:
#     num1 = int(input('enter the number: '))
#
# except:
#     print('Invalid values! ')
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('end kod')
#########################################
'''отоброжение ошибки
1. import sys'''

# list_ = [1,2,3,4,5]
# index = int(input('vedite index '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error')

'''2. Exception as e / (error)'''
# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('vedite index'))
#         print(ls[index])
#     except Exception as e:
#         print(f'ooops we catched {e.__class__} error')

# try:
#     num1 = int(input('enter number'))
#     print(num1 / 0)
# except ValueError:
#     print('Invalid values')
# except ZeroDivisionError:
#     print('Divide by')
##########################
#
# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('Na nol / delit nelzia')
# except ValueError:
#     print('Invalid sinvol!')
# else:
#     print(result)
# finally:
#     print('The end!!! ')
'''Колкулятор новая версия'''

# from string import digits
#
# flag = True
# symbols = digits + '-' + '.'
#
# while flag:
#     num1 = input('vedite')
#     num2 = input('vedite2')
#     try:
#
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except:
#         print('vy veli ne pravelno')
#         continue
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
