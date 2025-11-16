numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = list(filter(lambda x: x % 2 == 1, numbers))

print(numbers)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[1:2]

print(fruits)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
del numbers[3:5]

print(numbers)

cities = ["New York", "London", "Tokyo", "Moscow", "Paris"]
cities.pop(2)

print(cities)