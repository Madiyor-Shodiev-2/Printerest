# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     print(a)
# else:
#     print(b)

# #2
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# max = a 

#3
start = 0
while True:
    x = int(input("N sonini kiriting: "))
    n = "fizzbuzz" if x % 3 == 0 and x % 5 == 0 else \
        "fizz" if x % 3 == 0 else \
        "buzz" if x % 5 == 0 else \
        str(x)
    start += 1
    if start == 10:
        break
    print(n)
#4

