
# მომხმარებელს შეეკითხეთ სწავლობს თუარა გოაში, თუ სწავლობს შეეკითხეთ ომელ ჯგუფშია, თუ პასუხი
#  იქნება ჯგუფი13 შეეკითეთ რომ არის თუ არა გაბრიელი მისი მენტორი, თუ პასუხი იქნება კი უთხარით
# რომ თქვენც აქ სწავლობთ და ნამდვილად გაბრიელია ორივეს მენტორი, თუ პასუხი არიქნება გაბრიელი ყველა
#  სხვა შემთხვევაში დაუბეჭდეთ რომ ის ტყუის და არარის სინამდვილეში ჯგუფ13-ში 😉



def check_student():
    goa_student = input("Hello! Are you studying in Goa? (yes/no): ").strip().lower()
    
    if goa_student == "yes":
        group = input("Which group are you in? ").strip().lower()
        
        if group == "group13":
            mentor = input("Is Gabriel your mentor? (yes/no): ").strip().lower()
            
            if mentor == "yes":
                print("I also study here and indeed, Gabriel is both of our mentor!")
            else:
                print("You are lying, you are not actually in group13")
        else:
            print("You are lying, you are not actually in group13")
    else:
        print("You are lying, you are not actually in group13")
