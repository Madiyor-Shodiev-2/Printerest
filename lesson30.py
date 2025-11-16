total = 0
for number in range(1, 101):
    total += number
print(total)
#2
total = 0
odd, even = 0, 0
for number in range(1, 51):
    if number % 2 == 0:
        odd += number
    else:
        even += number
print(f"It's Odd: {odd}. It's even: {even}")
#3
count_division_7 = 0
for number in range(-80, 81):
    if number % 7 == 0:
        count_division_7 += 1
print(count_division_7)
#4
fruits = ['olma','banan','apelsin','olma']
count_apple = 0
for fruit in fruits:
    if fruit == 'olma':
        count_apple += 1
print(count_apple)
#5
