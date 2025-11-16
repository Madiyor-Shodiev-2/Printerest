#Boolean17
even = 567
is_hundred_splace_and_odd = 567 < 1000 and 567 % 2 == 1

#Boolean18
a, b, c = 9, 18, 9
is_two_are_equal = (a == b or b == c or c == a)
print(is_two_are_equal)

#01100
#10101

#Boolean19
a, b, c = 12, 21, 36

#Boolean20
a, b, c = 12, 21, 26
isRandom = (a != b and b != c and a != c)

#Boolean21
x = 154
a, b, c = x // 100, (x % 100 - x % 10) // 10, x % 10

if a < b and b < c:
    print("It's true")

#Boolean22
x = 321
a, b, c = x // 100, (x % 100 - x % 10) // 10, x % 10

if a < b and b < c or a > b and b > c:
    print("It's true")

#Boolean23
palindrome = 757
a, c = palindrome // 100, palindrome % 10

if a == c:
    print("It's palindrone number")

#Boolean24
A, B, C = 12, 45, 67
D = pow(B, 2) * -4 * A * C

if A*pow(D, 2) + B * D + c == 0:
    print("It's true discriminant")

#Boolean25
x, y = -1, 25
if x < 0 and y > 0:
    print("Ha ikkinchi jumalaga kiradi!")

#Boolean26
x, y = 12, -5
if x > 0 and y < 0:
    print("Ha ikkinchi jumlaga kiradi!")

#Boolean27
x, y = 78, 156
if x < 0 and y > 0 or x < 0 and y < 0:
    print("Bu ikkinchisiga va uchinchisiga kiriladi!")

#Boolean28
x, y = 12, 67
if x > 0 and y > 0 or x < 0 and y < 0:
    print("Bu birinchi va uchinchi jihatga kiradi!")

#Boolean29
x,y = 2, 4
x1, y1 = 15, 16
x2, y2 = 17, 18
if x1 <= x <= x2 and y2 <= y <= y1:
    print("Jumla tortburchak ichida joylashgan!")
else:
    print("Jumlar tortburchak ichida joylashmagan!")

#Boolean30
a, b, c = 12, 25, 67
if a == b == c and a > 0:
    print("Tog'ri javob berdingiz!")