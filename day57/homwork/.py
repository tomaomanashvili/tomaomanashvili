def sum_even_index(numbers):
    return sum(numbers[i] for i in range(len(numbers)) if i % 2 == 0)
def even_or_odd(number):
    return "ლუწია" if number % 2 == 0 else "კენტია"
numbers_list = [1, 2, 3, 4, 5, 6]
print(sum_even_index(numbers_list))  


number = 7
print(even_or_odd(number))  

