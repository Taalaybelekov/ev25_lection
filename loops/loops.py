# цыклы - это конструкция при помоши которых можно организовать многократное
#           испольнение определенного кода
# while - <expression>:
#     <body>
# <else>:
#     <body>
   #######################
# i = 0
# while i <= 10:
#
#     print(f'цикл выполнился {i} раз')
#     i+=1
# else:
#     print('конец цикла')
# print('начала кода')
################################
# name1 = ''
# name2 = ''
# i = 0
# while name1.lower()!= 'john' and name2.lower()!= 'jamie':
#     name1 = input('Vedite imya1: ')
#     name2 = input('Vrdite imya2: ')
#     i+=1
#     if i > 4:
#         print('цикл остановлен ')
#         break
# else:
#     print('vy veli pravelnoe imya: ')
###############################################
# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None
#
# while username !=admin[0] or password !=admin[1]:
#     username = input('vedite username: ')
#     password = input('Vedite password: ')
#     i-=1
#     if i == 0:
#         print('Vy zablakirovany!!! ')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zashli v sistemu! ')

#########################################
# for <variable> in <iterable object>
#     <body>
# list_ =[0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) то же самое можно зделать через цикл for
#
# for x in list_:
#     print(x)
#################################################
#
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for x in ls:
#     print(f'element: {x}')
#################################
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# i = 0
# while i < len(ls):
#     print(f'element:{i}')
#     i+=1

##################################################
# secret_list = ['DeltaViski', 'LOTR123','JohnSnow']
# word = input('vedite secrtet kod')
# while word not in secret_list: # крутит пока не будет слово из секрет листа
#     print('Incorect word Try one more time')
#     word =input('Vedite secred kod')
# print(f'You are welcom, {word}')

###################################################

# steps = 8
# path = 'UDDDUDUU'
# res = 1
# sea_level = 0
# verh = 'U'
# vniz = 'D'
# k_dol= 0
# for x in path:
#     if x==verh:
#         sea_level +=1
#     elif x==vniz:
#         sea_level-=1
#     if x==verh and sea_level==0:
#       k_dol+=1
#
# print(k_dol)
#пример второй
# steps = 9
# path = 'UDDUUDDUU'
# # res = 2
# sea_level = 0
# dolina = 0
# for x in path:
#     if x=='U':
#         sea_level +=1
#         if sea_level == 0:
#             dolina +=1
#     elif x == 'D':
#         sea_level-=1
# print(dolina)

# n1 =input('ведите имя и фамилию').split(' ')
# n2 = input('ведите имя и фамилию').split(' ')
# n3 = input('ведите имя и фамилию').split(' ')
# n4 = input('ведите имя и фамилию').split(' ')
# n5 = input('ведите имя и фамилию').split(' ')
#
# name=[n1[-1],n2[-1],n3[-1],n4[-1],n5[-1]]
# print(name)
# name.sort()
# print(name)

#
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# for x in lists:
#     if x==max(lists):
#         print('MAX',x)
#         break
# for x in lists:
#     if x==min(lists):
#         print('MIN',x)
#         break

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# dubl = [x for i, x in enumerate(list_) if i != list_.index(x)]
# print(dubl)
################################################

num = [1,1,2,3,5,8,13,21,34,55,89]
for i in num:
    if i<5:
        
        print(i)
