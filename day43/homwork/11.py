import datetime
current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")
