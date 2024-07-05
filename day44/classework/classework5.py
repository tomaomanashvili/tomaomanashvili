 #  5) Enter a number to the user and then using a for loop output the sum of all the numbers up to this number
 #  (for example, if he enters 10, output the sum of all the numbers up to 10, for example). 




user_input = int(input("Enter a number: "))


total_sum = 0


for i in range(1, user_input + 1):
    total_sum += i


print(f"The sum of all numbers up to {user_input} is {total_sum}.")




