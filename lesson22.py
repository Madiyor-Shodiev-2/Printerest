#integer1
L = 12
print(L / 100)

#integer2
M = 100
print(M/1000)

#integer3
file_bite_size = 1024
print(file_bite_size / 1024) 

#integer4
A = 12
B = 3
print("Kesmani shuncha marta A ga joylashtirsa boladi", A // B)

#integer5
A = 24
B = 5
print("Kesmaga joylashmagan qismi", A % B)

#integer6
number = 24
print(number)
print(bin(number))

#integer7
number = 50
print(sum(range(0, number+1)))

#integer8
number = 67
number = number // 10 + (number % 10 * 10)
print(number)

#integer9
number3 = 523
print(number3 // 100)

#integer10
number = 678
print(number % 10)
print((number % 100 - number % 10)//10)

#integer11
number = 100
print(sum(range(0, number+1)))

#integer12
number = 123
snumber = number % 10 * 100 + (number % 100 - number % 10) + number // 100
print(snumber) 

#integer13
number = 123
number = str(number % 100) + str(number//100)
print(number)

#integer14
number = 123
number = str(number % 10) + str(number//10)
print(number)

#integer15
number = 567
number = (number % 100 - number % 10) * 10 + number // 100 * 10 + number % 10
print(number)

#integer16
number = 478
number = (number // 100) * 100 + number % 100 // 10 + number % 10 * 10
print(number)

#integer17
number = 5297
number = number % 10000 // 1000
print(number)