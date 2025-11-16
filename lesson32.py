# vertical = 1
# while vertical <= 4:
#     gorizontal = 1
#     while gorizontal <= 4:
#         print("*", end="")
#         gorizontal += 1
#     print()
#     vertical += 1

# vertical = 1
# while vertical <= 4:
#     gorizontal = 1
#     print("#", end="")
#     while gorizontal <= 3:
#         print("*", end="")
#         gorizontal += 1
#     print()
#     vertical += 1

# print("####")
# vertical = 1
# while vertical <= 3:
#     gorizontal = 1
#     print("#", end="")
#     while gorizontal <= 3:
#         print("*", end="")
#         gorizontal += 1
#     print()
#     vertical += 1

# print("####")
# vertical = 1
# while vertical <= 3:
#     gorizontal = 1
#     print("#", end="")
#     while gorizontal <= 2:
#         print("*", end="")
#         gorizontal += 1
#     print("#", end="")
#     print()
#     vertical += 1
# print("####")

# oddOrEven = 1
# vertical = 1
# result = ""
# while vertical <= 5:
#     goryzontal = 1
#     if oddOrEven == 1:
#         oddOrEven = 2
#         while goryzontal <= 4:
#             result += "#"
#             goryzontal += 1
#         result += "\n"
#     else:
#         oddOrEven = 1
#         while goryzontal <= 4:
#             if goryzontal in [1, 4]:
#                   result += "#"
#             else:
#                   result += "*"
#             goryzontal += 1
#         result += "\n"
#     vertical += 1
# print(result)

# vertical = 1
# oddOrEven = 1
# while vertical <= 5:
#     goryzontal = 1
#     if oddOrEven == 1:
#         oddOrEven = 2
#         while goryzontal <= 5:
#             print("#", end="")
#             goryzontal += 1
#     else:
#         oddOrEven = 1
#         while goryzontal <= 5:
#             if goryzontal % 2 == 0:
#                 print("0", end="")
#             else:
#                 print("#", end="")
#             goryzontal += 1
#     print()
#     vertical += 1

# vertical = 1
# success = 1
# result = ""
# while vertical <= 5:
#     goryzontal = 1
#     while goryzontal <= 5:
#         if goryzontal == success:
#             result += "0"
#         else:
#             result += "*"
#         goryzontal += 1
#     result += "\n"
#     success += 1
#     vertical += 1
# print(result)

# vertical = 1
# max_success = 1
# result = ""
# while vertical <= 8:
#     goryzontal = 1
#     while goryzontal <= 8:
#         if goryzontal in range(1, max_success+1):
#             result += "0"
#         else:
#             result += "*"
#         goryzontal += 1
#     result += "\n"
#     max_success += 1
#     vertical += 1
# print(result)

# vertical = 1
# ZeroOrOne = 0
# while vertical <= 5:
#     goryzontal = 1
#     while goryzontal <= 5:
#         if ZeroOrOne == 0:
#             print(ZeroOrOne, end="")
#             ZeroOrOne = 1
#         else:
#             print(ZeroOrOne, end="")
#             ZeroOrOne = 0
#         goryzontal += 1
#     print()
#     vertical += 1

zerro_array = [1, 5]
vertical = 1
while vertical <= 5:
    goryzontal = 1
    while goryzontal <= 5:
        if goryzontal in zerro_array:
            print("\033[31m0\033[0m", end="")
        else:
            print("1", end="")
        goryzontal += 1
    zerro_array[0] += 1
    zerro_array[1] -= 1
    print()
    vertical += 1