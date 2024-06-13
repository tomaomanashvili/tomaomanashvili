def main():
    # შექმენით სია თქვენი საყვარელი მანქანის სახელებით
    cars = ["audi", "wolsvagen", "golf gtr", "mercedes", "BMW"]

    # შემდეგი ნაწილი გადააკეთეთ ელემენტის შეცვლა
    undesired_car = "Ford"
    new_car = "Mercedes"

    if undesired_car in cars:
        index = cars.index(undesired_car)
        cars[index] = new_car

    # დაბეჭდეთ სია ყველა ელემენტით
    print("სია ყველა ელემენტით:")
    for car in cars:
        print(car)

if __name__ == "__main__":
    main()
