numbers = []
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

greater_than_100 = [num for num in numbers if num > 100]
less_than_100 = [num for num in numbers if num <= 100]

print("Numbers greater than 100:", greater_than_100)
print("Numbers less than or equal to 100:", less_than_100)
