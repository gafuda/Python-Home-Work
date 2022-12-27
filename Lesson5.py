# from random import randint

# max_value = 100
# k = int(input('Введите натуральную степень k:'))
# coefficient = [randint(0, max_value) for i in range(k)]+[randint(1, max_value)]

# a = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
#     j in enumerate(coefficient) if j][::-1])
# a = a.replace('x^1+', 'x+')
# a = a.replace('x^0', '')
# a += ('', '1')[a[-1] == '+']
# a = (a, a[:-2])[a[-2:] == '^1']

# print(a)


# with open('1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('1.txt', 'r') as file:
#     1 = file.readline()
#     list_of_1 = 1.split()


# with open('2.txt', 'r') as file:
#     2 = file.readline()
#     list_of_2 = 2.split()

# print(f'{list_of_1} + {list_of_2}')
# sum_poly = list_of_1 + list_of_2

# with open('sum.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_1} + {list_of_2}')
