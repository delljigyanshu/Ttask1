#list:
my_list = [10,20,30,40,50,60,70,80,90,100]

# #adding an element in the list:

# my_list.append(110)
# print(my_list)

# #remove an element in the list:

# my_list.remove(50)
# print(my_list)

# #modifying an element in the list:

# my_list[5] = 130
# print(my_list)

# #reverse the element in the list:

# my_list.reverse()
# print(my_list)

#dictionary:
# my_dict = {'name':'jigy','age':20,'city':'uttar pradesh'}

# #adding an element in the dictionary:

# my_dict['gender']='Male'
# my_dict['hobby']='guitar'
# print(my_dict)

# #remove an element in the dictionary:

# del my_dict['gender']
# print(my_dict)

# #modify an element in the dictionary:

# my_dict['city']='goa'
# print(my_dict)


# #reverse the element in the dictionary:

# reversed_dict = {v: k for k, v in my_dict.items()}
# print(reversed_dict)

#set:
my_set = {10,20,30,40,50,50,60,60,70,80,90,100}

#adding an element in the set:

# my_set.add(120)
# my_set=sorted(my_set)
# print(my_set)

#remove an element in the set:

# my_set.remove(40)
# my_set=sorted(my_set)
# print(my_set)

#modify an element in the set:

# my_set.add(140)
# my_set.discard(20)
# my_set=sorted(my_set)
# print(my_set)

# #reverse an element in the set:

my_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
my_list = sorted(my_set)
my_list.reverse()
print(my_list)
