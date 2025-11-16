number = int(input("Son kiriting: "))
words = ("#" * number) + "##" 

print(words)

for i in range(1, number + 1):
    print("#", end="")
    for a in range(1, number + 1):
        print("*", end="")
    print("#")    

print(words)