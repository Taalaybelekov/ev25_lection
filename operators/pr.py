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
from string import digits

flag = True
symbols = digits + '-' + '.'

while flag:
    is_correct_number = True
    num1 = input(' vedite pervoe chislo : ')

    if len(num1) <= 1 and (num1 == '.' or num1 == '-') and num1:
            is_correct_number = False
    for x in num1:

        if x not in symbols:
            print(' Vy veli nepravelnoe chislo')
            is_correct_number = False
            break
    num2 = input(' vedite pervoe chislo 2: ')

    if len(num2) <= 1 and (num2 == '.' or num2 == '-') and num2:
            is_correct_number = False
    for x in num2:

        if x not in symbols:
            print(' Vy veli nepravelnoe chislo')
            is_correct_number = False
            break
    if not is_correct_number:
            continue
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    # print(num1)
    # print(num2)
    what = input('что делаем (+.-.*./.%.**.//): ')

    if what == '+':
        res = num1 + num2
        print('Результат: '+str(res))
    elif what == '-':
        res = num1 - num2
        print('Результат: '+str(res))
    elif what == '*':
        res = num1 * num2
        print('Результат: '+str(res))
    elif what == '/':
        if num2 == 0:
            print('на ноль нельзя делить')
        else:
            print(f'Результат: {num1 / num2}')
    elif what == '%':
        res = num1 % num2
        print('Результат: '+str(res))
    elif what == '**':
        res = num1 ** num2
        print('Результат: '+str(res))
    elif what == '//':
        res = num1 // num2
        print('Результат: '+str(res))
    else:
        print('Вы ввели неправельную операцию')

    choice = input('Hotite ostanovit (yes)' )
    if choice.lower() == 'yes':
        flag = False
        print('Poka')


