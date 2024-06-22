numbers = []
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print("Even numbers:", evens)
print("Odd numbers:", odds)
