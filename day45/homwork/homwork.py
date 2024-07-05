def calculate_sum_and_below_average(numbers):
    
    total_sum = sum(numbers)
    print(f"რიცხვების ჯამი: {total_sum}")

    
    average = total_sum / len(numbers)
    print(f"საშუალო მაჩვენებელი: {average:.2f}")


    below_average = [num for num in numbers if num < average]
    print("რიცხვები, რომლებიც საშუალოზე ნაკლებია:")
    for num in below_average:
        print(num)


numbers = [12, 45, 23, 67, 34, 89, 19, 37, 40]


calculate_sum_and_below_average(numbers)
