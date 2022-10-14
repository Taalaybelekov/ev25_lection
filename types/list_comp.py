

# ls = [x for x in range(0,201) if x%2==0]
# print(ls)

# ls1 = [x for x in range(0,201,2)]
# print(ls1)

# list: 0 - 100 -> x%2 == 0 and x%3 ==0
# ls = [x for x in range (0, 300) if x % 2==0 and x%3==0]
# print(ls)
# ls =[]
# for x in range(0,300):
#     if x%2==0 and x%3==0:
#         ls.append(x)
#     print(ls)
##################################################

#list 0-100 -> x%2==0: x**2, x%3==0: x**3;
#
# ls= []
# for x in range(0,101):
#     if x%2 ==0:
#         ls.append(x**2)
#     elif x%3==0:
#         ls.append(x**3)
# print(ls)
# ls = [x**2 if x%2==0 else x**3 for x in range(0,101) if x%2==0 or x%3==0]
# print(ls)
############################################################################
#newlist =[expression for item in interable <if condition ==True]

# ls =[str(i**2) for i in range(0,11)]
# print(ls)

#ls =[[1,2,3],[4,5,6],[7,8,9]]
#result = [1,2,3,4,5,6,7,8,9]
#(ls =[*ls[0],*ls[1],*ls[2]] - так только если знаешь точное количество)
# #print(ls)

#ls =[[1,2,3],[4,5,6],[7,8,9]]
# res=[]
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)

# ################
# from datetime import datetime
# stat= datetime.now()
# ls = [x for x in range(0,100_000_000)] -работает быстрее обычного
# # ls = []
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# finish = datetime.now()
# print(finish-stat)
# ##############################################
# dict_ ={
#     'key1': 'value1',
#     ':key2': 'value2'
# }
# dict_ = {x: x**2 for x in range(1, 15)}
# print(dict_)
###################
# names = ['John', 'Tirion','Eygan','Sansa','Ramsi']
# dict_ = {name: names.index(name) for name in names}
# print(dict_)
# ########################################
# dict1 = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4,
#     'e': 5, 'f': 6, 'g': 7, 'h': 8
# }
# # 'a' : 'нечетное', 'b': 'четное'
# res ={}
# for k,v in dict1.items():
#     if v % 2 ==0:
#         res[k]= 'четное'
#     else:
#         res[k]='нечетное'
# print(res)

# dict1 = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4,
#     'e': 5, 'f': 6, 'g': 7, 'h': 8
# }
# res = {k: 'четное' if v %2 ==0 else 'нечетное' for k, v in dict1.items()}
# print(res)
#######################################
# list_ =[i for i in range(1,100)]
# print(list_)

# list_=[n for n in range(1, 51) if not n%2==0]
# print(list_)
#
# list_ = [-4, -3, -2, -1,0, 1, 2, 3, 4]
# int_list = [n for n in list_ if n>0 and n%2==0]
# print(int_list)
#
# list_ = [x**2 for x in range(1, 26) if x**2]
# print(list_)
#
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)

#x**2 if x%2==0 else x
# list_ = [x**2 if x%2==0 else x for x in range(1,11)]
# print(list_)
#
# list_ =[True if x%2==0 else False for x in range(1,11)]
# print(list_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(x)<=4 else 'longer' for x in list_name]
# print(new_list)


# dict_ = {num:num**2 for num in range(1,11) }
# print(dict_)

"""Задание 12

Создайте словарь dict_ где ключами будут строки, а значениями произвольные
числа. Затем пройдитесь по элементам и запишите в a вместо значения
строку 'even', если значение четное, а если нет то 'odd'.

Например, если у нас есть словарь:

dict_ = {'first': 1, 'second': 2, 'third': 3}

То результатом будет:

{'first': 'odd', 'second': 'even', 'third': 'odd'}

Нужно использовать comprehension."""


# dict_ = {'first':1, 'second':2, 'third':3}
# dict_ = {k:'even' if v%2==0 else 'odd' for k,v in dict_.items()}
# print(dict_)


 # string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

# s = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# l = len(s)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integ.append(int(s_int))
#
# print(integ)

# s = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# word_list = s.split()
# num_list = []
#
# for word in word_list:
#     if word.isnumeric():
#         num_list.append(int(word))
#
# print(num_list)
#
# ???????????
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# word_list = string_.split()
# list_ = []
#
# for word in word_list:
#     if word.isnumeric():
#         list_.append(int(word))
#
# print(list_)

#######################
# list_ = [x*2 if x%2==0 for x in range(0,11) ]
# print(list_)

# list_ = [ x for x in range(1,11)]
# print(list_)

# list_= range(0,11)
# res= []
# for x in list_:
#     if x%2==0:
#         res.append(x/2)
# print(res)

# ls = [x/2 for x in range(0,11) if x%2==0]
# print(ls)
