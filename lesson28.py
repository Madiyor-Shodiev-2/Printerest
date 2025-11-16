x = 50
if x > 0:
    x+=1
print(x)

#if2
x = 82
if x > 0:
    x+=1
else:
    x-=2
#if3
x = 78
if x == 0:
    x *= 10
elif x > 0:
    x += 1
else:
    x -= 2
#if4
a, b, c = 9, 18, 27
start = 0
for x in [a,b,c]:
    if x > 0:
        start+=1
print(start)
#if5
a, b, c = 90, -18, -27
positive, negative = 0, 0
for x in [a, b, c]:
    if x >= 0:
        positive += 1
    else:
        negative += 1
#if6
x, y = 89, 67
if x > y:
    print("X kotta")
else:
    print("Y kotta")
#if7
x, y = 100, 121
if x < y:
    for i in range(0, x):
        print(i + " ", end="")
else:
    for i in range(0, y):
        print(i + " ", end="")
#if8
x, y = 19, 79
if x > y:
    print(f"Eng kottasi {x}")
    print(f"Eng kichigi {y}")
else:
    print(f"Eng kottasi {y}")
    print(f"Eng kichigi {y}")
#if9
A, B = 19, 81
if A > B:
    A = B
    B += 1
print(A + " " + B)
#if10
A, B = 36, 89
if A != B:
    A = A + B
    B = A + B
else:
    A, B = 0
    