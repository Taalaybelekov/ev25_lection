# s1 ='America'
# s2 ='Japan'
# fir_s1 = s1[0]
# fir_s2 = s2[0]
# mid_s1 =s1[len(s1)//2]
# mid_s2 =s2[len(s2)//2]
# las_s1 = s1[-1]
# las_s2 = s2[-1]
# res = fir_s1+fir_s2+mid_s1+mid_s2+las_s1+las_s2
# print(res)
####################
# dano [1--100]
# число /3 -> fu
# число /5 -> ba
# число /3, /5 ->fuba
# вывод 3 fu
#     5 ba
#     15 fuba

# for number in range(1, 100):
#     print(number)
#     if number % 3==0 and namber % 5==0:
#         print(f'{number} fuba')
#     elif number % 3 == 0:
#         print(f'{number}fu')
#     elif number %5 ==0:
#         print(f'{number} ba') посмотреть и исправить код
###############################################################

import random

ls =['Plov', 'Manty','Kuurdak','lagman','Oromo']
p = 0
m = 0
k = 0
l = 0
o = 0
for x in range(0, 100000):
   #print(x)
    choice = random.choice(ls)
    print(choice)
    if choice.lower() =='plov':
        p += 1
    elif choice.lower() == 'mantu':
        m +=1
    elif choice.lower() == 'kuurdak':
        k +=1
    elif choice.lower() =='lagman':
        l +=1
    else:
        o=+1
print(f'Plov:{p} \n Manty:{m} \n Kuurdak:{k} \n Lagman:{l} \n Oromo:{o}')

lis = [p,m,k,l,o]
# print(lis)
resl = max(lis)
print(resl)
if resl==p:
    print('Plov')
elif resl==m:
    print('Manty')
elif resl==k:
    print('Kuurdak')
elif resl==l:
    print('Lagman')
else:
    print('Oromo')
