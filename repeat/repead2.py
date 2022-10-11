# range(stat,stop=,[step]) -возврашает последовательность из целых чисел, начиная с старт
# до стоп , возвращает итерируемый тип данных range

# x = range(1,10)
# print(x)
# for num in x:
#     print(num)
##############################
# x =range(1,10,2)
# print(list(x))

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n =3
# list1 = []
# list2 = []
# list3 = []
# for x in range(0, len(list_), n):
#
#     list1.append(list_[x])
#     list2.append(list_[x+1])
#     if x+2 >=len(list_):
#         continue
#     list3.append(list_[x+2])
# print(list1)
# print(list2)
# print(list3)
############################################
# res =[]
# for x in range(0,3):
#     ls=[]
#     for x in range(0,3):
#         ls.append(0)
#     res.append(ls)
#
# print(res)

#Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# list_ = [1, 2, 3]
# Результат:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
#
# from itertools import permutations
# list_ = [1, 2, 3]
# res = list(permutations([1,2,3]))
# print(res)
