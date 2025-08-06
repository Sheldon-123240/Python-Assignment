#My List
my_list = [ 13, 45 ,64 ,45]

#New List
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("My_list:", my_list)

my_list.insert(1,15)
print("My_list:", my_list)

my_list2 = [50, 60, 70]

my_list.extend(my_list2)
print("My_list:", my_list)

my_list.remove(70)
print("My_list:", my_list)

my_list.sort() #In ascending order
print("My_list:", my_list)

print(my_list[4])