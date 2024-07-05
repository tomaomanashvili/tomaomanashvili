#Print even numbers separately and odd numbers separately from 0 to 100 inclusive for loop ის გამოყენებით 


even_numbers = []
odd_numbers = []


for number in range(101):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)


print("Even numbers from 0 to 100:")
print(even_numbers)


print("Odd numbers from 0 to 100:")
print(odd_numbers)

