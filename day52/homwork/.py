import random

def get_computer_choice():
    choices = ["ქვა", "ქაღალდი", "მაკრატელი"]
    return random.choice(choices)

def get_user_choice():
    choice = input("შეიყვანეთ თქვენი არჩევანი (ქვა, ქაღალდი, მაკრატელი): ").strip().lower()
    if choice == "ქვა" or choice == "ქაღალდი" or choice == "მაკრატელი":
        return choice
    else:
        print("არასწორი არჩევანი. სცადეთ ხელახლა.")
        return get_user_choice()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ფრეა!"
    elif (user_choice == "ქვა" and computer_choice == "მაკრატელი") or \
         (user_choice == "ქაღალდი" and computer_choice == "ქვა") or \
         (user_choice == "მაკრატელი" and computer_choice == "ქაღალდი"):
        return "თქვენ მოიგეთ!"
    else:
        return "თქვენ დამარცხდით!"

def play_game():
    print("კეთილი იყოს თქვენი მობრძანება ჩიფოუმის თამაშში!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"თქვენ აირჩიეთ: {user_choice}")
    print(f"კომპიუტერმა აირჩია: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
v