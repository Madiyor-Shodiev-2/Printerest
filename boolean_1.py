#Boolean1
A = 45
isPrimary = A > 0

if isPrimary:
    print("A soni musbat")

#Boolean2
A = 45
isEven = A % 2 == 1

if isEven:
    print("A soni toq son")

#Boolean3
A = 45
isOdd = A % 2 == 0

if isOdd:
    print("A soni Juft son")

#Boolean4
A, B = 3, 3
inInterval = A > 2 and 3 >= B 

if inInterval:
    print("Yes, its just to 2 ... 3")

#Boolean5
A, B = 0, -3
isTrue = A >= 0 or B < -2

#Boolean6
A, B, C = 120, 12, 840
isTrue = A <= B <= C
print(type(isTrue))

#Boolean7
A, B, C = 12, 24, 56
isTrue = A <= B <= C

#Boolean8
A, B = 13, 7
isTrue = (A+B)%2==0
# print(isTrue)

#Boolean9
A, B = 7, 2
isTrue = A % 2 == 1 or B % 2 == 1

#Boolean10
A, B = 7, 9
isTrue = (A % 2 == 0 and B % 2 != 0) or (B % 2 == 0 and A % 2 != 0)

#Boolean11
A, B = 4, 2
isTrue = (A+B)%2==0
print(isTrue)

#Boolean12
A, B, C = 23, 46, 68
isEven = A >= 0 and B >= 0 and C >= 0
print(isEven)

#Boolean13
evenOf = A >= 0 or B >= 0 or C >= 0

#Boolean14
usJustOneEven = (A * B * C) <= 0

#Boolean15
isJustTwoEven = (A >= 0 and B >= 0 and C < 0) or (A < 0 and B >= 0 and C >= 0) or (A >= 0 and B < 0 and C >= 0)

#Boolean16
even = 45
isTwo = even < 100 and even % 2 == 0 