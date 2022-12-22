###########################################
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print ("Начальный список: " + str(x))
# total = 0
# for i in range(1, len(x), 2):
#     total += x[i]       
# print("Сумма: " + str(total))

###########################################
# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

###########################################
# lst = [1.1, 1.2, 3.1, 5, 10.01]
# lst2 = [round(i%1,2) for i in lst]
# print(lst, ', разница: ', max(lst2) - min(lst2))

###########################################
# задачу с десятичными числами не поняла даже из интернета, копипастить впустую не хочу :(

###########################################
# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))