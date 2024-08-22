# მომხმარებელს შემოატანინეთ ორი რიცხვი
num1 = int(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = int(input("შემოიტანეთ მეორე რიცხვი: "))

# სხვადასხვა არითმეტიკული ოპერაციების შედეგების გამოთვლა
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
floor_division = num1 // num2

# შედეგების დაბეჭდვა
print("ჯამი:", addition)
print("გამოკლება:", subtraction)
print("გამრავლება:", multiplication)
print("განაყოფი:", division)
print("მოდულუსი (ნაშთი):", modulus)
print("მთელმოყოფითი:", floor_division)
age = int(input("შემოიტანეთ თქვენი ასაკი: "))

if age > 18 and age < 20:
    print("თქვენი ასაკი არის 18-ზე მეტი და 20-ზე ნაკლები.")
else:
    print("თქვენი ასაკი არ არის ამ დიაპაზონში.")
# მაგალითები
print(5 > 3)   # True
print(5 < 3)   # False
print(5 >= 5)  # True
print(5 <= 6)  # True
print(5 != 4)  # True
print(5 == 5)  # True
# მომხმარებელს შემოატანინეთ ორი რიცხვი
whole_number = int(input("შემოიტანეთ მთელი რიცხვი: "))
decimal_number = float(input("შემოიტანეთ ათწილადი რიცხვი: "))

# მონაცემთა ტიპების დაბეჭდვა
print("მთელი რიცხვის ტიპი:", type(whole_number))
print("ათწილადის ტიპი:", type(decimal_number))
integer_var = 10
float_var = 10.5
string_var = "Hello"
boolean_var = True

print("integer_var ტიპი:", type(integer_var))
print("float_var ტიპი:", type(float_var))
print("string_var ტიპი:", type(string_var))
print("boolean_var ტიპი:", type(boolean_var))
day_number = int(input("შემოიტანეთ რიცხვი 1-დან 7-მდე: "))

if day_number == 1:
    print("ორშაბათი")
elif day_number == 2:
    print("სამშაბათი")
elif day_number == 3:
    print("ოთხშაბათი")
elif day_number == 4:
    print("ხუთშაბათი")
elif day_number == 5:
    print("პარასკევი")
elif day_number == 6:
    print("შაბათი")
elif day_number == 7:
    print("კვირა")
else:
    print("არასწორი რიცხვი")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")
    i += 1
age = int(input("შემოიტანეთ თქვენი ასაკი: "))

if age > 5 and age < 12:
    print("თქვენ ხართ ბავშვი")
elif age >= 12 and age < 18:
    print("თქვენ ხართ თინეიჯერი")
elif age >= 18:
    print("თქვენ ხართ ზრდასრული")
else:
    print("ასაკი არ შეესაბამება არც ერთ კატეგორიას")
budget = float(input("შემოიტანეთ თქვენი ბიუჯეტი: "))
price = float(input("შემოიტანეთ ნივთის ფასი: "))

if budget >= price:
    print("თქვენ შეგიძლიათ შეიძინოთ ეს ნივთი.")
else:
    print("თქვენ არ გაქვთ საკმარისი თანხა.")
