# from math import modf, ceil

###########################################
# array = [2, 3, 5, 9]
# #        0  1  2  3
#
# answer = 0
#
# for index in range(0, len(array), 2):
#    answer += array[index]
#    print(f"Index: {index}\tValue: {array[index]}")
#
# print(answer)

###########################################
# array = [2, 3, 4, 5, 6]
#
# answer = []
#
# for index in range(0, ceil(len(array) / 2), 1):
#     answer.append(array[index] * array[-index - 1])
#
# print(answer)

###########################################
# array = [1.1, 1.2, 3.1, 5, 10.01]
#
# fractions = []
# for item in array:
#     fractions.append(item % 1)
#
# print(max(fractions) - min(fractions))
###########################################
# print(bin(45)[2:])

###########################################
# k = 8
# def fibonacci(n):
#     answer = []
#     x, y = 1, 1
#     for i in range(n):
#         answer.append(x)
#         x, y = y, x + y
#     x, y = 0, 1
#     for i in range(n + 1):
#         answer.insert(0, x)
#         x, y = y, x - y

#     return answer


# print(fibonacci(k))