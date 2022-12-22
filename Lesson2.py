###########################################
# num = float(input("Введите число: "))
# a = int(num)
# b = (num - a)
# b = b * 10**(len(str(b))-2)
# sum = 0
# while a > 0:
#     sum += a % 10
#     a //= 10
# while b > 0:
#     sum += b % 10
#     b //= 10
# print(int(sum))

###########################################
# from msilib import sequence

# n = int(input('Введите число: ')) \\\\ сама решение найти не смогла, возилась с библиотеками, 
#                                   \\\\ стащила из интернета. Но честно разобралась
# def get_squerence(n):              
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))

###########################################
# import random
# list = input("Введите числа через пробел (не менее 3х): ").split()
# print ("Начальный список: " + str(list))

# for i in range(len(list)-1, 0, -1): 
#     a = random.randint(0, i + 1) 
#     list[i], list[a] = list[a], list[i] 

# print ("Перемешанный список: " +  str(list))
