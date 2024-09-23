#Challenges
#challenge 1
# digits = "225424272163254474441338664823"
# #digits = "2846286484444288886666448822244466688822247"
# result = []
# scounter = counter = 0
# endcounter = len(digits)
# while counter < endcounter-1:
#     a = int(digits[counter])
#     b = int(digits[counter+1])
#     counter += 1
#     if a % 2 != b % 2:
#         if counter == endcounter - 1:
#             result.append(digits[scounter:counter+1])
#         continue
#     else:
#         result.append(digits[scounter:counter])
#         scounter = counter
# print(result)
# print(max(result, key=len))
#challenge 2
# def snakefill(n):
#     board_size = n * n
#     snake = 0
#     while 2**snake < board_size:
#         snake += 1
#     print(snake-1)
#
# snakefill(24)
#challenge 3
# def seq_level(*args):
#     lst = list(args)
#     for i in range(3):
#         lst, res = check(lst)
#         if res:
#             if i == 0:
#                 print("Linear")
#                 break
#             elif i == 1:
#                 print("Quadratic")
#                 break
#             elif i == 2:
#                 print("Cubic")
#
# def check(lst):
#     rlst = [lst[ctr+1] - lst[ctr] for ctr in range(len(lst)-1)]
#     slst = set(rlst)
#     flag = True if len(slst) == 1 else False
#     return rlst, flag
#
# seq_level(3, 6, 10, 15, 21)
#challenge 4
# def concert_seat(args):
#         # column_seat = [[row[x] for row in args] for x in range(len(args[0]))]
#         # for data in column_seat:
#         #     if not all(data[i] < data[i + 1] for i in range(len(data) - 1)):
#         #         return False
#         # return True
#
#         return all(sorted(set(row)) == list(row) for row in zip(*args))
#
# # print(concert_seat([[1, 2, 3, 2, 1, 1],
# # [2, 4, 4, 3, 2, 2],
# # [5, 5, 5, 10, 4, 4],
# # [6, 6, 7, 6, 5, 5]]))
#
# print(concert_seat([[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]))
#challenge 5
# def challenge5(lst, num):
#     nlst = [[lst[i] % 2 == 0, lst[i+1] % 2 == 0] for i in range(len(lst)-1)]
#     if num % 2 != 0:
#         return sum([1 for element in nlst if not (element[0] == True and element[1] == True)])
#     else:
#         return sum([1 for element in nlst if not (element[0] == False and element[1] == False)])
#
# lst1 = [0, 4, 6, 8]
# print(challenge5(lst1, 12))
#challenge 6
# def atbash(txt):
#     a = ord('a')
#     A = ord('A')
#     z = ord('z')
#     Z = ord('Z')
#     cypher = lambda s: ''.join([chr(Z - (ord(letter) - A)) if letter.isupper() else chr(z - (ord(letter) - a)) if letter.isalpha() else letter for letter in txt])
#     return cypher(txt)
# print(atbash("Christmas is the 25th of December"))
# newword = ""
# for letter in txt:
#     if letter.isalpha():
#         lord = ord(letter)
#         if letter.isupper():
#                 newword += chr(Z - (lord - A))
#         else:
#                 newword += chr(z - (lord - a))
#     else:
#         newword += letter
# challenge 7
def zeroesToEnd(lst):
    lst.sort(key=lambda x: x == 0)
    return lst
    # for element in lst:
    #     if element == 0:
    #         lst.remove(element)
    #         lst.append(0)
    # return lst
print(zeroesToEnd([0, 0, 2, 0, 5]))