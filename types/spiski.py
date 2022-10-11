# list()- Список (моссив) - изменяемый ,последовательный тип данных, который
# предоставляет из себя колекцию каких либо объектов (значений)

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

####################################
# range() - возврашает последовательность элементов (чисел)

# ls = list(range(1, 101))
# print(ls)
# print(type(ls))
# ls1 = list(range(0,101,2)) #- третий параметь range это шаг
# print(ls1)

###########################################################

# ls = list(range(1, 101))
# for num in ls:
#     print(num)
# print(num)
# print('finished for! ')
###############################
# ls = list(range(1, 101))
# for num in ls:
#     #print(num * 2 if num % 2 ==0 else num ** 3)
#     if num % 2 ==0:
#         print(f'Число {num} четное, квадрат: {num **2} ')
#     else:
#          print(f'Число {num} не четное, куб: {num **3} ')
##############################################
# Методы списков :
# print(dir(list))
    # append - добовляет элемент в конце списка
# ls = [1,2,3]
# print(ls)
# ls.append('hello')
# ls.append([6,7,8])
# ls.append(True)
# print(ls)
##############################################
# extent(iterable) - раширяет список элементами из iterable object
# ls = [1,2,3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)
###
# ls = [1,2,3]
# ls.append([4,5,6])
# print(ls)
# ls.extend([4,5,6])
# print(ls)
###########################################

#insert(<index>, <element>) - добовляет элемент по указонному индехсу
# ls = ['string', 2, 3, False]
# ls.insert(1,4)
# ls.insert(-1, True)
# ls.insert(20, True) #если индек больше элементов в списке то тогда встанет в конец
# print(ls)
###################################################################
# index(element, [start], [end])- возвращает индех элемента в списке
#ls = ['Hello', 'World', 'my', 'name', 'is', 'John']
# res =ls.index('name')
# print(res)
# print((ls[res]))
# print(ls[0:2])
###############################
#count(element) - возврашает количетсво вхожденний элементов в списке
# ls = [1, 2, 3, 4, 5, 6, 5, 5, 5]
# res = ls.count(5)
# print(res)
###################

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'queen', 'USA']
# print(ls)
# str1 = input('Vvedite slovo: ')
# if str1 in ls:
#     print(f'{str1} есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('net!')
#########################################
# sort() - сортирует список, если в аргументах передать reverse = True то список будет отсортирован
# в убывающем порядке

# import random
# ls = []
# for x in range(0,50):
#     ls.append(random.randint(0, 1000))
# print(ls)
# print()
# ls.sort()
# print(ls)
# print()

# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aikol', 'Nurayim', 'makers']
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)
# ls.sort(reverse=True, key=len)
# print(ls)
##########################################
# remove(element) -удаляет элемент из списка , если такого нет то он выводит ошибку
# pop([index]) - удаляет и возвращает элемент по индехсу. но елсли индекс не указан он удаляет
# последний элемент

# ls = [5, 1, 2, 4, 5, 5, 5]
# #ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)
# print(ls)
#################
# ls = [5, 1, 2, 4, 5, 5, 5]
# delet = ls.pop(0)
# print(ls)
# print(delet)
###############
# ls = [5, 1, 2, 4, 5, 5, 5, 99]
# delet = ls.pop()
# print(ls)
# print(delet)
##################
#update -------
# ls = [1, 'h',3]
# print(ls)
# ls[1] = 2
# print(ls)

# labels = ['mers', 'honda','niva']
# for i in labels:
#     print(f'I like brand {i}')

# name_of_list = ['Helloworld']
# new_list = name_of_list[0]
# print(new_list)


# word = 'Helloworld'
# half1 = word[:int((len(word)+1)/2)]
# half2 = word[int((len(word)+1)/2):]
# word1 = half2 + half1
# word1.split(word1)
# print(type(word1))
# for n in word1:
#     print(n)


#
# list = ['world','hello']
# a = list.pop(0)
# list.append(a)
# print(list)
# # if list:
# #     list.insert(0, list.pop())

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# print(suitcase)
# suitcase.pop()
# print(suitcase)
# suitcase.insert(0,'панама')
# print(suitcase)


# lists = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# res = 0
# for x in range(len(lists)):
#   if type(lists[x]) == type(int()):
#     res = res+lists[x]
# print(res)

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# for n in lists:
#    print(len(n))





