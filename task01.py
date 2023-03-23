import os
os.system('cls')

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

count_n = int(input('Введите кол-во элементов первого массива: '))
n=[]
for i in range(1,count_n+1):
     n.append(int(input(f'Введите {i} элемент первого массива: ')))

count_m = int(input('Введите кол-во элементов второго массива: '))
m=[]
for i in range(1,count_m+1):
     m.append(int(input(f'Введите {i} элемент второго массива массива: ')))
k = []
count_k = 0
for i in range(0, count_m):
    if m[i] in n:
        k.append(m[i])
        count_k +=1
print(n)
print(m)
print(sorted(set(k)))
























# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

