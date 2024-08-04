def calculator():
    num1 = float(input("შემოიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შემოიტანეთ მეორე რიცხვი: "))
    operation = input("აირჩიეთ მოქმედება (მიმატება, გამოკლება, გამრავლება, გაყოფა): ").strip().lower()

    if operation == "მიმატება":
        result = num1 + num2
    elif operation == "გამოკლება":
        result = num1 - num2
    elif operation == "გამრავლება":
        result = num1 * num2
    elif operation == "გაყოფა":
        if num2 != 0:
            result = num1 / num2
        else:
            return "გაყოფა ნულზე შეუძლებელია."
    else:
        return "არასწორი მოქმედება."

    return f"შედეგი: {result}"
def sum_of_list(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(f"რიცხვების ჯამი: {sum_of_list(numbers)}")
def average_of_list(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(f"რიცხვების საშუალო არითმეტიკული: {average_of_list(numbers)}")
def odd_or_even():
    number = int(input("შემოიტანეთ რიცხვი: "))
    if number % 2 == 0:
        return f"{number} არის ლუწი."
    else:
        return f"{number} არის კენტი."

print(odd_or_even())
def time_travel():
    current_age = int(input("შემოიტანეთ თქვენი ახლანდელი ასაკი: "))
    current_year = int(input("შემოიტანეთ ამჟამინდელი წელი: "))
    travel_years = int(input("რამდენი ხანი გსურთ დროში მოგზაურობა: "))
    direction = input("გსურთ წარსულში მოგზაურობა თუ მომავალში (წარსული/მომავალი): ").strip().lower()

    if direction == "მომავალი":
        new_year = current_year + travel_years
        new_age = current_age + travel_years
    elif direction == "წარსული":
        new_year = current_year - travel_years
        new_age = current_age - travel_years
        if new_age < 0:
            return "თქვენ ვერ იქნებით ნეგატიური ასაკის."
    else:
        return "არასწორი მიმართულება."

    return f"დროში მოგზაურობის შემდეგ წელი იქნება {new_year} და თქვენი ასაკი იქნება {new_age} წელი."

print(time_travel())