#set- хранит только уникальные значение
#################################
# Множества в питоне это Контейнер который содержит
# в себе уникальные элементы в неупарядоченном виде
# {}
# # set
# a={1:'a'} это словарь
# a={1,2,3} это множества
########################################
# set_={8,1,2,3,4,5,6,7,7,7,7,}
# print(set_)
# print(type(set_))
#######################
#
# ls = [1,2, 'a',0,False,True,'n','b']
# str1= 'My name is John Snow'
# ls.extend(str1)
# print(ls)
# res = list(set(ls))
# print(res)



# ls = [1,2, 'a',0,False,True,'n','b']
# str1= 'My name is John Snow'
# ls.extend(str1)
# print(ls)
# set1 = {*ls} #- второй способ
# print(set1)
# res = [*set1]
# print(res)

##########################################################
# a = {1,2,3,4,5}
# print(a)
# a.pop()
# print(a)
# a.remove(3)
# print(a)
# a.discard(233) - # это тоже удаляет но только если нет элемента то он не выдает ошибку
#######################################
# set_ = {1,2,3,4,5,6,7}
# set_.discard(8)
# print(set_)
# set_.discard(6)
# print(set_)
#############################################################################
# #frozenset - замороженное множества
# a = {1,2,3,4,5}
# f_set = frozenset([1,2,3,4,5,6])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)
# print(dir(frozenset))

#
# a = set('gwerty')
# b = frozenset('qwerty')
# a.add(1)
# print(a)
# а на фрезенсет не сможеш добовлять

# Составьте код которая принимает номер месяца вашего рождения и
# в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона:
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным».

# Важно учесть, что пользователи могут ввести любой
# тип данных в качестве аргумента (не попадитесь на этом
# и предупредите о том, что «Требуется ввести реальный номер месяца»).
#
# months = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'July',
#     8: 'Avgust',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'Desember'
# }
# while True:
#     number = input('Vedite nomer mesyasa: ')
#     if number =='john':
#         break
#     if not number.isdigit():
#         print('trebuetsia vesti realnyi nomer mesiasa')
#         continue
#     number = int(number)
#     if number not in range(1,13):
#         print('trebuetsia vesti realnyi nomer')
#     if number in range(3, 6):
#         print(f'Вы родилис в {months[number]} Птицы пели прекрасные песни')
#
#     elif number in range(6, 9):
#         print(f'Вы родилис в {months[number]} Светило солнце')
#
#     elif number in range(9, 12):
#         print(f'Вы родилис в {months[number]} Уражай был невероятным')
#
#     else:
#         print(f'Вы родилис в {months[number]} Снег')


