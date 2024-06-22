numbers = []
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

two_digit_count = sum(1 for num in numbers if 10 <= num < 100)
print("Number of two-digit numbers:", two_digit_count)
numbers = [int(input("Enter a number: ")) for _ in range(10)]
sum_of_multiples_of_five = sum(num for num in numbers if num % 5 == 0)
print("Sum of multiples of five:", sum_of_multiples_of_five)
