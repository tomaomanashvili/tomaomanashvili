
my_list = []


elements_to_add = [10, 20, 30, 40, 50, 60, 70]
my_list.extend(elements_to_add)


my_list[2], my_list[3] = my_list[3], my_list[2]



my_list.insert(4, 1000000)


my_list.pop(5)
my_list.pop(0)


print(my_list)

[20, 40, 30, 1000000, 60, 70]


