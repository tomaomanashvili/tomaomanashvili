my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    print(item)
user_list = []
for _ in range(1000):
    item = input("რისი დამატება გსურთ სიაში? ")
    user_list.append(item)
print(user_list)
user_list = []
for _ in range(1000):
    item = input("რისი დამატება გსურთ სიაში? ")
    if len(item) <= 6:
        user_list.append(item)
print(user_list)
outer_list = []
list1 = [1, 2, 3]
list2 = [4, 5, 6]
outer_list.append(list1)
outer_list.append(list2)

for sublist in outer_list:
    for item in sublist:
        print(item)
names = ["John", "Doe"]
full_name = " ".join(names)
print(full_name)
# 1. მოცემული სიის დაბეჭდვა
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    print(item)

# 2. მომხმარებელს 1000-ჯერ კითხვის პროცესი და სიის შექმნა
user_list = []
for _ in range(1000):
    item = input("რისი დამატება გსურთ სიაში? ")
    user_list.append(item)
print(user_list)

# 3. სიის შექმნა და არჩეული სიტყვების დამატება 6 ასოზე ნაკლები სიგრძით
user_list = []
for _ in range(1000):
    item = input("რისი დამატება გსურთ სიაში? ")
    if len(item) <= 6:
        user_list.append(item)
print(user_list)

# 4. ორი სიის დამატება ცარიელ სიაში და გადატარება for loop-ში
outer_list = []
list1 = [1, 2, 3]
list2 = [4, 5, 6]
outer_list.append(list1)
outer_list.append(list2)

for sublist in outer_list:
    for item in sublist:
        print(item)

# 5. სახელის და გვარის სტრინგების შეჯამება ერთ ცვლადში
names = ["John", "Doe"]
full_name = " ".join(names)
print(full_name)
# შევქმნათ ქართული მამაპაპური სია სახელად S_A_Q_A_R_T_V_E_L_O
S_A_Q_A_R_T_V_E_L_O = []

# მომხმარებელს შევეკითხოთ ქართველი ფეხბურთელების სახელები 12-ჯერ
for _ in range(12):
    player_name = input("გთხოვთ მიუთითეთ ქართველი ფეხბურთელის სახელი: ")
    S_A_Q_A_R_T_V_E_L_O.append(player_name)

# დავპრინტოთ სია
print(S_A_Q_A_R_T_V_E_L_O)
