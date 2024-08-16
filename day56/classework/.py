for i in range(1, 51):
    if i % 5 == 0:
        print(i)

product = 1
for i in range(5, 11):
    product *= i
print(product)
number = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
if number % 2 == 0:
    result = number / 2
else:
    result = number * 3 + 1
print(result)
number = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
if number % 2 == 0:
    result = number / 2
else:
    result = number * 3 + 1
print(result)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def rectangle_area(length, width):
    return length * width
def rectangle_perimeter(a, b, c, d):
    return a + b + c + d
def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)
def min_max(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    
    print(f"მინიმალური რიცხვი: {min_num}")
    print(f"მაქსიმალური რიცხვი: {max_num}")
def sum_even_index(numbers):
    total = 0
    for i in range(0, len(numbers), 2):
        total += numbers[i]
    return total
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"
