import random


first_string = open("C:\\Users\\makri\\Desktop\\hokku\\first.txt","r")
second_string = open("C:\\Users\\makri\\Desktop\\hokku\\second.txt","r")
third_string = open("C:\\Users\\makri\\Desktop\\hokku\\third.txt","r")
list_first = []
list_second = []
list_third = []
for line1 in first_string:
    list_first.append(line1)
for line2 in second_string:
    list_second.append(line2)
for line3 in third_string:
    list_third.append(line3)
choice_first_string = random.choice(list_first)
choice_second_string = random.choice(list_second)
choice_third_string = random.choice(list_third)


print(choice_first_string)
print(choice_second_string)
print(choice_third_string)