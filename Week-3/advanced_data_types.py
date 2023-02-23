# advanced data types
#mutable vs immutable
#mutable are data types that can be change/edited during program life cycle
#add/remove elements
#immutable are data types that cannot be edited during program life cycle

#1)lists is mutable
friends = ["mark","john","paul","luke"]

students = ["marie","kigen","seenphine"]
friends.extend(students)
friends.append("matthew")
friends.pop()
friends.sort()
friends.reverse()
# or friengs = [] for empty lists
#--> append extend


#2)tuples are immutable
#type of list that are immutable use ()
'''
stationaries = ("pens","ink","sharpener","stapler")
# you can replace the whole tuple
stationaries = ("ruler","clipboard","eraser")
for stationary in stationaries:
    print(stationary)

numbers =(1,2,3,4,5,6,7,8,9)
print(numbers)


#3)dictionaries/dict
#uses key and value
student = {"name" :"mark", "age" : 18,"gender" :"male","is_tall": True}
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])

#create a dictionary of your friends detail
#fav_colour,hobby,course,weight,team,height
friend = {"fav_colour" :"blue","hobby" :"skating","course" :"civil engeneering","weight" : 68,"height" :170}
print(friend["fav_colour"])
print(friend["hobby"])
print(friend["course"])
print(friend["height"])
print(friend["weight"])
print(student.values())
print(student.keys())
'''
#name : "mark" --> name(key), "mark"(value)
my_fruits ={"apple","pineapple","cherry","banana","orange"}
for fruit in my_fruits:
    print(my_fruits)
    print(type(my_fruits))
    print(len(my_fruits))