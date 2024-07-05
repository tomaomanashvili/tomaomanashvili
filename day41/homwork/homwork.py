def sum_of_multiples_of_five(numbers):

    multiples_of_five = [num for num in numbers if num % 5 == 0]
    
    
    total_sum = sum(multiples_of_five)
    
  
    print("ხუთის ჯერადი რიცხვების ჯამი:", total_sum)


numbers = [10, 21, 35, 40, 56, 70, 83, 95]


sum_of_multiples_of_ffive(numbers) # type: ignore
