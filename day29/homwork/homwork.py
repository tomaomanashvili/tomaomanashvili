#ვისაც ბოლო საკლასო დავალება სრულად არ გაგიკეთებიათ შეასრულეთ სრულად, სწორი სტრუქტურით
#( შექმენით ფორმა სადაც გექნებათ input ველები: ემაილი, პაროლი, სახელი, გვარი, ტელეფონის ნომერი,
#  submit ღილაკი. გამოიყენეთ ყველაფერი დღევანდელი ნასწავლი მასალისგან რათა მოხდეს შეყვანილი ინფორმაციის 
# სწორად გადაგზავნა ( name, value ) )




def main():

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    
   
    form_data = {
        "Email": email,
        "Password": password,
        "First Name": first_name,
        "Last Name": last_name,
        "Phone Number": phone_number
    }
    

    print("\nSubmitted Form Data:")
    for key, value in form_data.items():
        print(f"{key}: {value}")
    
    
    
if __name__ == "__main__":
    main()
