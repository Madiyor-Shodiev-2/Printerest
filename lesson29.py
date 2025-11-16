total = 0
while True:
    x = int(input("Raqam kiriting: "))
    if x != 0:
        total += x
    else:
        print(total) 
        break

#2-task
A, B = 0, 10
total = 0
while A < B:
    total += A
    A += 1
#3-task
list = input("Please insert list")
index, total = 0, 0
dynamic_list = []
string_number = ""
while index < len(list):
    if list[index] != " ":
        string_number += list[index]
    else:
        dynamic_list.append(int(string_number))
        string_number = ""
    index += 1
dynamic_list.append(int(string_number))
print(dynamic_list)
#4-task
x = [1,2,3,14,5,6,6,7]
count_x = len(x)
big_one = 0
index = 0
while index < count_x:
    if big_one < x[index]:
        big_one = x[index]
    index += 1
print(big_one)
#5-task
